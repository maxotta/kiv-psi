package psi.websockets.chat;

import java.io.IOException;
import java.util.HashMap;
import java.util.Set;
import java.util.concurrent.CopyOnWriteArraySet;

import javax.websocket.OnClose;
import javax.websocket.OnError;
import javax.websocket.OnMessage;
import javax.websocket.OnOpen;
import javax.websocket.Session;
import javax.websocket.server.PathParam;
import javax.websocket.server.ServerEndpoint;

@ServerEndpoint(value="/chat/{nickname}")
public class WebSocketChatEndpoint {
 
    private Session session;
    private static Set<WebSocketChatEndpoint> chatEndpoints 
      = new CopyOnWriteArraySet<>();
    private static HashMap<String, String> users = new HashMap<>();

    @OnOpen
    public void onOpen(
      Session session, 
      @PathParam("nickname") String nickname) throws IOException {
 
        this.session = session;
        chatEndpoints.add(this);
        users.put(session.getId(), nickname);

        String from = users.get(session.getId());
        broadcast("(+) " + from + " has joined the chat.");
    }

    @OnMessage
    public void onMessage(Session session, String message) 
      throws IOException {
        String from = users.get(session.getId());
        broadcast(" * " + from + ": " + message);
    }

    @OnClose
    public void onClose(Session session) throws IOException {
 
        chatEndpoints.remove(this);
        String from = users.get(session.getId());
        broadcast("(-) " + from + " has left the chat.");
        users.remove(session.getId());
    }

    @OnError
    public void onError(Session session, Throwable throwable) {
        // Do error handling here
    }

    private static void broadcast(String message) 
      throws IOException {
 
        chatEndpoints.forEach(endpoint -> {
            synchronized (endpoint) {
                try {
                    endpoint.session.getBasicRemote().
                      sendText(message);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });
    }
}

