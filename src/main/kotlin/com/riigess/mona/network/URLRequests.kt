package com.riigess.mona.network

import com.beust.klaxon.JsonObject
import com.beust.klaxon.Parser
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.Response

class URLRequests {
//    private val baseURL:String = "https://discord.com/api/v10"
//    private val wssURL:String = "wss://gateway.discord.gg"
    private val baseURL:String = "http://192.168.15.11:20080"

    init {
        println(baseURL)
    }

    fun makeGetRequest(endpoint:String): Response {
        val client = OkHttpClient()
        val request = Request.Builder()
            .url("$baseURL/$endpoint")
            .get()
            .build()
        return client.newCall(request).execute()
    }

    fun convertToJsonObject(str:String): JsonObject {
        val s:StringBuilder = StringBuilder().append(str)
        val parser = Parser.default()
        val jsonObj = parser.parse(rawValue = s) as JsonObject
        return jsonObj
    }

    fun medsDumpWithMap(jsonObj:JsonObject, key:String) {
        val jsonArr = jsonObj.map.get(key) as List<Map<String, String>>
        for(i in 0..jsonArr.size-1) {
            print("ID:")
            println(jsonArr.get(i).get("id"))
            print("\tmed_name:")
            println(jsonArr.get(i).get("med_name"))
            print("\tTimestamp:")
            println(jsonArr.get(i).get("timestamp"))
        }
    }
}
