package com.riigess.mona


//import java.io.File
//import java.util.Properties
import dev.kord.core.event.message.MessageCreateEvent
import dev.kord.gateway.Intent
import dev.kord.gateway.PrivilegedIntent
import dev.kord.core.Kord
import dev.kord.core.on
import kotlinx.coroutines.Dispatchers
import kotlin.concurrent.thread

class Runner {
    companion object {
        @JvmStatic
        public final fun main(args: Array<String>) {
//            Runner().discordStartCoroutine()
            suspend {
                Runner().discord()
            }
        }
    }

    fun discordStartCoroutine() {
        suspend {
                discord()
        }
    }

    suspend fun discord() {
        val envVar: String = System.getenv("discord_token") ?: ""
        val kord = Kord(envVar)

        kord.on<MessageCreateEvent> {
            if (message.author?.isBot == true) return@on
            if (message.content == "!ping") message.channel.createMessage("pong")
        }

        kord.login {
            presence { playing("!ping to pong") }

            @OptIn(PrivilegedIntent::class)
            intents += Intent.MessageContent
        }
    }
}
