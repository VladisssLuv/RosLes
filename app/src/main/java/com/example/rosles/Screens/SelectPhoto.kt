package com.example.rosles.Screens

import android.Manifest
import android.app.Dialog
import android.content.ActivityNotFoundException
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.Bitmap
import android.graphics.Color
import android.location.LocationManager
import android.net.Uri
import android.os.Bundle
import android.os.Environment
import android.provider.MediaStore
import android.view.View
import android.widget.*
import androidx.appcompat.app.ActionBar
import androidx.core.app.ActivityCompat
import androidx.core.view.get
import com.example.rosles.DBCountWood
import com.example.rosles.R
import com.example.rosles.databinding.ScreenPhotoBinding
import java.io.File
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter


class SelectPhoto:BaseAppClass() {


    private val db = DBCountWood(this, null)


    var latitude: Double? = 0.0
    var longitude: Double? = 0.0
    val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
    var photobuf:Bitmap?=null
    var id_sample=0
    private val REQUEST_TAKE_PHOTO = 1
    private lateinit var binding: ScreenPhotoBinding
    private lateinit var locationManager: LocationManager


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ScreenPhotoBinding.inflate(layoutInflater)
        setContentView(binding.root)
        //инциализация навигации
        supportActionBar!!.displayOptions = ActionBar.DISPLAY_SHOW_CUSTOM
        supportActionBar!!.setDisplayShowCustomEnabled(true)
        supportActionBar!!.setCustomView(R.layout.custom_action_bar)

        // проверяем что разрешение получено
        id_sample=intent.getIntExtra("id_sample",98)
        setLocation()

        db.getphotoall()

        inittable()

        val view: View = supportActionBar!!.customView

        binding.toolbar.reload.visibility = View.GONE

        binding.toolbar.save.visibility = View.GONE

        binding.toolbar.addbutton.setOnClickListener {
            //     getContent.launch("image/*")
            val takePictureIntent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
            try {
                startActivityForResult(takePictureIntent, REQUEST_TAKE_PHOTO)
            } catch (e: ActivityNotFoundException) {
                e.printStackTrace()
            }
        }
        binding.toolbar.delete.visibility=View.GONE

    }

    private fun setLocation() {

        // проверяем что разрешение получено
        locationManager = getSystemService(Context.LOCATION_SERVICE) as LocationManager

        // Проверяем разрешения на использование местоположения
        if (ActivityCompat.checkSelfPermission(
                this,
                Manifest.permission.ACCESS_FINE_LOCATION
            ) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(
                this,
                Manifest.permission.ACCESS_COARSE_LOCATION
            ) != PackageManager.PERMISSION_GRANTED
        ) {
            ActivityCompat.requestPermissions(
                this,
                arrayOf(
                    Manifest.permission.ACCESS_FINE_LOCATION,
                    Manifest.permission.ACCESS_COARSE_LOCATION
                ),
                1
            )
            return
        }

        // Получаем местоположение пользователя
        val location = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER)

        if (location == null) {
            Toast.makeText(this, "Включите GPS", Toast.LENGTH_SHORT).show()
        } else {
            latitude = location!!.latitude
            longitude = location.longitude
        }

    }



    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if (requestCode == REQUEST_TAKE_PHOTO && resultCode == RESULT_OK) {
            // Фотка сделана, извлекаем миниатюру картинки
            val thumbnailBitmap = data?.extras?.get("data") as Bitmap


        }

        if (requestCode === 1 && resultCode === RESULT_OK) {
            // Проверяем, содержит ли результат маленькую картинку
            if (data != null) {
                if (data.hasExtra("data")) {
                    val thumbnailBitmap: Bitmap? = data.getParcelableExtra("data")
                    // Какие-то действия с миниатюрой

                    val temp=GPStracker(this)

                    db.writephoto(temp.bitmap_to_base(thumbnailBitmap), id_sample,latitude,longitude,LocalDateTime.now().format(formatter).toString())

                }
            }
        }
    }


    override fun onRestart() {
        val buf= binding.tblLayout.getChildAt(0)
        binding.tblLayout.removeAllViews()
        binding.tblLayout.addView(buf)
        inittable()
        super.onRestart()
    }
    fun inittable(){

        var activetableRow: TableRow? = null
        val list=db.getphoto(id_sample)

        list.forEach {
            val tableRow = TableRow(this)

            val text1=TextView(this)
            val text2=TextView(this)
            val text3=TextView(this)
            val text4=TextView(this)
            val photo=it.photo

            text1.setText(it.photo.toString().substringAfter('@'))
            text2.setText(it.latitude.toString())
            text3.setText(it.longitude.toString())
            text4.setText(it.date.format(formatter).toString())

            val textvalues=listOf(text1, text2, text3, text4)
            textvalues.forEach {
                it.textAlignment=View.TEXT_ALIGNMENT_CENTER
                it.setTextColor(-0x1000000)
                tableRow.addView(it)
            }
            tableRow.setOnClickListener{
                photobuf=photo
                activetableRow?.setBackgroundResource(R.color.color_transporent)
                tableRow.setBackgroundResource(R.color.color_transporent)
                activetableRow = tableRow
                activetableRow!!.setBackgroundResource(R.color.activecolumn)
            }
            binding.tblLayout.addView(tableRow)
        }

        binding.toolbar.open.setOnClickListener{
            if(activetableRow!=null){
                val latitude = activetableRow?.get(1) as TextView
                val longitude = activetableRow?.get(2) as TextView
                val date_value = activetableRow?.get(3) as TextView
                val dialog: Dialog = Dialog(this)
                dialog.setContentView(R.layout.view_image_dialog)
                val image = dialog.findViewById<ImageView>(R.id.image_for_photo)
                val coords = dialog.findViewById<TextView>(R.id.value_coord)
                val date = dialog.findViewById<TextView>(R.id.value_date)
                val delete = dialog.findViewById<Button>(R.id.delete)
                image.setImageBitmap(photobuf)
                coords.setText("${latitude.text} ${longitude.text}")
                date.setText("${date_value.text}")
                dialog.show()
            }
        }

    }
}


//    чтение из файлов
//    val getContent = registerForActivityResult(GetContent()) { uri: Uri? ->
//        bitmap=MediaStore.Images.Media.getBitmap(contentResolver, Uri.parse(uri.toString()))
//        val tableRow = TableRow(this)
//        val text1= TextView(this)
//        val text2= TextView(this)
//
//        var file = File(uri.toString())
//
//        text1.setText(bitmap.toString())
//        text2.setText(LocalDateTime.now().toString())
//
//        tableRow.addView(text1)
//        tableRow.addView(text2)
//        tableRow.setOnClickListener {
//            binding.test.setImageBitmap(bitmap)
//        }
//        binding.tblLayout.addView(tableRow)
//    }






