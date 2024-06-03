package com.riigess.mona.network

import io.ktor.http.HttpMethod
import io.ktor.websocket.WebSocketSession
import io.ktor.websocket.Frame
import kotlinx.coroutines.runBlocking
import org.koin.core.component.inject
import sun.net.NetworkClient

class WebSocketClientManager(url:String) {
    private val networkClient: NetworkClient by inject()
    private val client = networkClient.getInstance()
    private val session = runBlocking {
        client.webSocketSession(method = HttpMethod.Get,
            host=url)
    }
    private val url:String

    init {
        this.url = url
    }

    suspend fun sendMessage(message:String) {
        try {
            session.outgoing.send(Frame.Text(message))
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

    suspend fun receiveMessage(message: (String) -> Unit) {
        try {
            client.webSocket(method=HttpMethod.Get, host=this.url) {
                session.incoming.consumeEach {

                }
            }
        } catch (e:Exception) {
            e.printStackTrace()
        }
    }
}