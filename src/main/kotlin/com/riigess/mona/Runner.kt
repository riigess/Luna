package com.riigess.mona

import com.beust.klaxon.JsonObject
import com.riigess.mona.network.URLRequests

class Runner {
    companion object {
        @JvmStatic
        public final fun main(args: Array<String>) {
            val req = URLRequests()
            val resp:String = req.makeGetRequest("/trazadone").body!!.string()
            val jsonObj:JsonObject = req.convertToJsonObject(resp)
            req.medsDumpWithMap(jsonObj, "data")
        }
    }
}
