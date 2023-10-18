// package <pkgName>;

import javax.swing.*;
import java.awt.*;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
	public static void main(String[] args) {
		JFrame obj  = new JFrame();
		obj.setBounds(10, 10, 700, 600); 
		obj.setBackground(new Color(0x252422));
		obj.setTitle("BallBreaker!");
		obj.setResizable(false);
		obj.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Gameplay game = new Gameplay();
		obj.add(game);
		obj.addKeyListener(game);
		
		obj.setVisible(true);
	}
}
