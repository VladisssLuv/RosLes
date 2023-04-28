package com.example.rosles.Screens

import android.annotation.SuppressLint
import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.isVisible
import com.example.rosles.Adapters.BaseInterface
import com.example.rosles.Adapters.ChoiceSubjectAdapter
import com.example.rosles.DBCountWood
import com.example.rosles.R
import com.example.rosles.ResponceClass.BaseRespObject
import com.example.rosles.databinding.ChoicesubjectBinding

class ChoiceLes : AppCompatActivity() {

    private lateinit var binding: ChoicesubjectBinding

    private val db = DBCountWood(this, null)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ChoicesubjectBinding.inflate(layoutInflater)
        val view = binding.root
        setContentView(view)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = ""
        binding.textView4.text="Выберите лесничество"

        var id = intent.getStringExtra("id")
        initcorutine(id!!.toInt())
    }
    @SuppressLint("Range", "SuspiciousIndentation")
    fun initcorutine(id:Int){
        var a : MutableList<BaseRespObject>  = mutableListOf()
        var lesnichList = db.getLesnich(id)

        for (i in 0..lesnichList.size-1) {
            a.add(lesnichList[i].toBaseRespObject())
        }

        var adapter = ChoiceSubjectAdapter(a,object : BaseInterface {

            override fun onClick(itemView: Any) {
                start(itemView as Int)
            }

            override fun onClickButton() {

            }
        })

        if (a.isEmpty()){
            binding.GuideRecycler.emptytext.isVisible=true
        }
        binding.GuideRecycler.GuideRecycler.adapter=adapter
    }
    fun start(itemView: Int) {
        val intent1 = Intent(this, ChoiceDistrict::class.java)
        intent1.putExtra("id",itemView.toString())
        intent1.putExtra("id_Vedomost",intent.getStringExtra("id_Vedomost"))

        startActivity(intent1)
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(com.example.rosles.R.menu.menu, menu)
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
}