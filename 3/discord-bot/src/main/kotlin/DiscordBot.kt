package course.ebiz

import io.ktor.server.application.*
import okhttp3.Request
import okhttp3.RequestBody
import okhttp3.MediaType
import okhttp3.OkHttpClient
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject

class DiscordBot {

    val botToken = "token"

    fun sendMessageToDiscordChannel(channelId: String,message: String) {
        val client = OkHttpClient()
        val url = "https://discord.com/api/v10/channels/$channelId/messages"
    
        val json = JSONObject()
        json.put("content", message)
    
        val requestBody = json.toString().toRequestBody("application/json; charset=utf-8".toMediaType())

        val request = Request.Builder()
            .url(url)
            .post(requestBody)
            .addHeader("Authorization", "Bot $botToken")
            .addHeader("Content-Type", "application/json")
            .build()
    
        val response = client.newCall(request).execute()
        if (response.isSuccessful) {
            println("Message sent successfully: ${response.body?.string()}")
        } else {
            println("Failed to send message: ${response.code} ${response.message}")
        }
    }

}