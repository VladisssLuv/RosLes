package com.example.rosles.Screens

import android.annotation.SuppressLint
import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.ArrayAdapter
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.rosles.DBCountWood
import com.example.rosles.R
import com.example.rosles.databinding.AddPorodBinding
import com.example.roslesdef.Models.SpinerItem
import java.util.*
import kotlin.collections.HashMap


class AddPorod : AppCompatActivity() {

    private lateinit var binding: AddPorodBinding
    private val db = DBCountWood(this, null)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = AddPorodBinding.inflate(layoutInflater)
        setContentView(binding.root)
        //инциализация навигации
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = "Добавление"
        initActivity()
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            android.R.id.home -> finish()
            R.id.main -> {
                startActivity(Intent(this, Dashboard::class.java))
            }
            R.id.itemperechet -> {
                startActivity(Intent(this, MainActivity::class.java))
            }
            R.id.itemgps -> {
                startActivity(Intent(this, gps_activity::class.java))
            }
            R.id.profile -> {
                startActivity(Intent(this, profile::class.java))
            }
        }
        return true
    }

    @SuppressLint("SuspiciousIndentation")
    fun initActivity() {
        val sPref = getSharedPreferences("PreferencesName", MODE_PRIVATE)
        val id = sPref.getString("id", "")!!.toInt()

        val countries= db.getallporodArray()
        val countries1= db.getallpodlesArray()

        val arrayAdapter =
            ArrayAdapter(this, android.R.layout.simple_spinner_item,countries )
        arrayAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)

        val arrayAdapter1 =
            ArrayAdapter(this, android.R.layout.simple_spinner_item, countries1)
        arrayAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        binding.les.adapter = arrayAdapter
        binding.podles.adapter = arrayAdapter1

        val hash = db.gethashFavoriteLes(id)

        val hashpodles = db.gethashFavoritepodLes(id)

        binding.buttonAuto.setOnClickListener {

            val valueles= binding.les.selectedItem as SpinerItem

            var flag=true
                hash.forEach { t, u ->
                if (u == valueles.name) {
                    flag=false
                    Toast.makeText(this, "Такая порода уже существует", Toast.LENGTH_SHORT).show()
                }
            }
            if (flag){
                db.addlesporod(id, valueles.id)
            }

            val valuepodles= binding.podles.selectedItem as SpinerItem
            var flagpodles = true

            hashpodles.forEach { t, u ->
                if (u == valuepodles.name) {
                    flagpodles = false
                    Toast.makeText(this, "Такая порода уже существует", Toast.LENGTH_SHORT).show()
                }
            }
            if (flagpodles){
                db.addpodlesporod(id, valuepodles.id)
            }
            finish()
        }

    }

    @SuppressLint("Range")
    fun getidbreed(value: String?,dbCountWood: DBCountWood):Int?{
        val cursor=dbCountWood.getallporod() // swap to getallporodArray()
        cursor.moveToFirst()
        val hash= HashMap<String,Int>()
        for (i in 1..cursor.getCount()){
            hash.put(
            cursor.getString(cursor.getColumnIndex("name_breed")),
            cursor.getString(cursor.getColumnIndex("id")).toInt())
            cursor.moveToNext()
        }
        cursor.close()
        return hash.get(value) // Q3?
    }

}

