package psi.websockets;

import java.io.IOException;
import java.util.Random;

import javax.websocket.OnOpen;
import javax.websocket.Session;
import javax.websocket.RemoteEndpoint.Basic;
import javax.websocket.server.ServerEndpoint;

@ServerEndpoint("/random")
public class WebSocketEndpoint {

    @OnOpen
    public void onOpen(Session session) throws IOException, InterruptedException {
        Basic client = session.getBasicRemote();
        Random random = new Random();
        int count = 0;
        int number;
        String message;
        for (;;) {
            count++;
            number = random.nextInt(100);
            message = count + ". => " + number;
            client.sendText(message);
            Thread.sleep(1000);
        }
    }
}

