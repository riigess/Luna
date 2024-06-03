package com.riigess.mona.discord

import com.riigess.mona.network.URLRequests
import io.ktor.client.HttpClient
import io.ktor.client.plugins.websocket.WebSockets
import io.ktor.client.plugins.websocket.webSocket
import io.ktor.http.HttpMethod
import io.ktor.websocket.Frame
import io.ktor.websocket.readText
import kotlinx.coroutines.runBlocking
import org.json.JSONObject

class Discord(token:String) {
    private val requests:URLRequests
    private val baseURL:String = "https://discord.com/api/v10"
    private val wssURL:String = "wss://gateway.discord.gg"
    private val token:String
    private val client:HttpClient
    private var interval:Int = -1

    init {
        this.token = token
        this.client = HttpClient {
            install(WebSockets)
        }
        this.requests = URLRequests(wssURL)
    }

    //TODO: Start the WebSocket connection, then make it asynchronously available (somehow)
    fun wss_login() {
        runBlocking {
            client.webSocket(method= HttpMethod.Get, host=wssURL, path="/?v=10&encoding=json") {
                val othersMessage = incoming.receive() as? Frame.Text ?: return@webSocket
                val jsonMessage = JSONObject(othersMessage.readText())
                if(jsonMessage.get("op") == 10) {
                    val temp = jsonMessage.getJSONObject("d")
                    interval = temp.getInt("heartbeat_interval")
                    val jitter: Double = temp.getDouble("jitter") // Does jitter exist?
                    val toSend: Frame.Text = Frame.Text("{\"op\":1}")
                    // Need to wait some amount of time determined by heartbeat * jitter
                    val toSleep: Long = (jitter * interval).toLong()
                    println("Sleeping for $toSleep seconds...")
                    Thread.sleep(toSleep)
                    println("Sending back op:1")
                    send(toSend)
                    print("Received: ")
                    println(incoming.receive() as? Frame.Text ?: return@webSocket)
                }
            }
        }
    }

    fun wssHeartbeat(sequenceNumber:Int) {
//        val heartbeatStructure = mapOf(Pair("op", 1), Pair("d", sequenceNumber))
        //TODO: Make a function for wss requests for Discord
//        makeWSSRequest(heartbeat_structure)
    }

    fun makeWSSRequest(message:Map<String, String>) {
    }

    fun makeNonWSSRequest(endpoint:String): Any {
//        val headers = mapOf(
//            "Authorization": "auth $this.token")
        val token = this.token
        val headers = mapOf(Pair("Authorization", "auth $token"),
                            Pair("accept", "application/json"))
        val resp = requests.makeGetRequest("$baseURL/$endpoint", headers=headers)
        return resp
    }
}