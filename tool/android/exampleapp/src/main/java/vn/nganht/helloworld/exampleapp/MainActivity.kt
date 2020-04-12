package vn.nganht.helloworld.exampleapp

import android.app.Activity
import android.os.Bundle
import android.view.ViewGroup
import android.widget.TextView
import vn.nganht.helloworld.TimeRepository

class MainActivity : Activity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val params = ViewGroup.LayoutParams(
            ViewGroup.LayoutParams.MATCH_PARENT,
            ViewGroup.LayoutParams.MATCH_PARENT
        )

        val textView = TextView(this).apply {
            text = CURRENT_TIME_MESSAGE_FMT.format(TimeRepository.getCurrentTime())
        }
        addContentView(textView, params)
    }

    companion object {
        const val CURRENT_TIME_MESSAGE_FMT = "Current time: %s"
    }
}
