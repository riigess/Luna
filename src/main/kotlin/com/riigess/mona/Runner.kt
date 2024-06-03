package com.riigess.mona

import com.riigess.mona.discord.Discord
import java.io.File
import java.util.*

class Runner {
    companion object {
        @JvmStatic
        public final fun main(args: Array<String>) {
            val file = File("settings.properties")
            val prop = Properties()
            prop.load(file.inputStream())
            val discord:Discord = Discord(prop.getProperty("discord"))
//            val temp = discord.makeNonWSSRequest("applications/@me")
            discord.wss_login()
//            print(temp)
        }
    }
}
