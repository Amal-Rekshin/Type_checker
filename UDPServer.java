import java.net.*;

public class UDPServer {
    public static void main(String[] args) {
        try (DatagramSocket socket = new DatagramSocket(9876)) {
            byte[] receiveBuffer = new byte[1024];
            DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
            socket.receive(receivePacket);
            String message = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("Received from client: " + message);

            String response = "hello client";
            byte[] sendBuffer = response.getBytes();
            InetAddress clientAddress = receivePacket.getAddress();
            int clientPort = receivePacket.getPort();
            DatagramPacket sendPacket = new DatagramPacket(sendBuffer, sendBuffer.length, clientAddress, clientPort);
            socket.send(sendPacket);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}