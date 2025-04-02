package course.ebiz

import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import io.ktor.server.html.*
import kotlinx.html.*

fun Application.configureRouting() {
    routing {
        get("/") {
            call.respondHtml {
                head {
                    title("Discord Message Sender")
                }
                body {
                    h1 { +"Send a message to Discord" }
                    form(action = "/send", method = FormMethod.post) {
                        p {
                            label {
                                +"Your message: "
                                textArea { name = "message"}
                            }
                        }
                        p {
                            submitInput { value = "Send Message" }
                        }
                    }
                }
            }
        }
        
        post("/send") {
            val parameters = call.receiveParameters()
            val message = parameters["message"]

            if (message.isNullOrBlank()) {
                call.respond(HttpStatusCode.BadRequest, "Message cannot be empty")
                return@post
            }
            
            val discordBot = DiscordBot()
            discordBot.sendMessageToDiscordChannel("763395258288570370", message)
            
            call.respondHtml {
                head {
                    title("Message Sent")
                }
                body {
                    h1 { +"Message sent to Discord!" }
                    p { +"Your message: $message" }
                    a(href = "/") { +"Send another message" }
                }
            }
        }
    }
}
