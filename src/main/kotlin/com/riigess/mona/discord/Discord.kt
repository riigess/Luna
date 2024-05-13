package com.riigess.mona.discord

import com.riigess.mona.network.URLRequests

class Discord(token:String) {
    private val requests:URLRequests = URLRequests()
    private val baseURL:String = "https://discord.com/api/v10"
    private val wssURL:String = "wss://gateway.discord.gg"
    private val token:String

    init {
        this.token = token
    }

    fun wss_login() {
    }

    fun wss_heartbeat() {
    }

    fun makeNonWSSRequest(endpoint:String) {
//        val headers = mapOf(
//            "Authorization": "auth $this.token")
        val headers = mapOf(Pair("Authorization", "auth $this.token"),
                            Pair("accept", "application/json"))
        val resp = requests.makeGetRequest("$baseURL/applications/@me")
    }
}