package brickBreaker;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class Gameplay extends JPanel implements KeyListener, ActionListener {
	private boolean play = false;
	private int score = 0;
	private int totBricks = 21;
	private Timer timer;
	private int delay = 8;
	private int playerPosX = 310;
	private int ballPosX = 120;
	private int ballPosY = 350;
	private int ballDirX = -1;
	private int ballDirY = -2;
	private MapGenerator map;
	public Gameplay(){
		map = new MapGenerator(3,7);
		addKeyListener(this);
		setFocusable(true);
		setFocusTraversalKeysEnabled(false);
		timer = new Timer(delay, this);
		timer.start();
	}
	
	public void paint(Graphics g){
		//background
		g.setColor(new Color(0x403D39));
		g.fillRect(1, 1, 692, 592);
		
		//scores
		g.setColor(new Color(0xEB5E28));
		g.setFont(new Font("noto sans", Font.BOLD, 25));
		g.drawString(""+score, 590, 30);
		
		//map
		map.draw((Graphics2D)g);
		//borders
		g.setColor(new Color(0x252422));
		g.fillRect(0, 0, 3, 592);
		g.fillRect(0,0,692, 3);
		g.fillRect(691, 0, 3, 592);
		
		//the paddle
		g.setColor(new Color(0xEB5E28));
		g.fill3DRect(playerPosX, 550, 100, 8, true);
		
		//ball
		g.setColor(new Color(0xFFFCF2));
		g.fillOval(ballPosX, ballPosY, 20, 20);
		
		//win
		if(totBricks <= 0){
			play = false;
			ballDirX = 0;
			ballDirY = 0;
			g.setColor(new Color(0xEB5E28));
			g.setFont(new Font("noto sans", Font.BOLD, 30));
			g.drawString("YOU WIN!\nSCORE:" + score, 230, 350);
			
			g.setFont(new Font("noto sans", Font.BOLD, 30));
			g.drawString("PRESS ENTER\nTO START", 190, 300);
		}
		
		//game over
		if(ballPosY > 570){
			play = false;
			ballDirX = 0;
			ballDirY = 0;
			g.setColor(new Color(0xEB5E28));
			g.setFont(new Font("noto sans", Font.BOLD, 30));
			g.drawString("GAME OVER!\nSCORE:" + score, 190, 300);
			
			g.setFont(new Font("noto sans", Font.BOLD, 30));
			g.drawString("PRESS ENTER\nTO START", 190, 300);
		}
		
		g.dispose();
	}
	
	public void actionPerformed(ActionEvent e){
		timer.start();
		
		if(play){
			//checking intersection
			if(new Rectangle(ballPosX, ballPosY, 20, 20).intersects(new Rectangle(playerPosX, 550, 100, 8))){
				ballDirY = -ballDirY;
			}
			
			A: for(int i=0;i<map.map.length;i++){
				for(int j=0;j<map.map[0].length;j++){
					if(map.map[i][j] > 0){
						int brickX = j*map.brickWidth + 80;
						int brickY = i*map.brickHeight + 50;
						int brickWidth = map.brickWidth;
						int brickHeight = map.brickHeight;
						
						Rectangle rect = new Rectangle(brickX, brickY, brickWidth, brickHeight);
						Rectangle ballRect = new Rectangle(ballPosX, ballPosY, 20, 20);
						Rectangle brickRect = rect;
						
						if(ballRect.intersects(brickRect)){
							map.setBrickVal(0, i, j);
							totBricks--;
							score += 5;
							
							if(ballPosX + 19 <= brickRect.x || ballPosX + 1 > brickRect.width){
								ballDirX = -ballDirX;
							}
							else{
								ballDirY = -ballDirY;
							}
							
							break A;
						}
					}
				}
			}
			
			ballPosX += ballDirX;
			ballPosY += ballDirY;
			if(ballPosX < 0){
				ballDirX = -ballDirX;
			}
			if(ballPosY < 0){
				ballDirY = -ballDirY;
			}
			if(ballPosX > 670){
				ballDirX = -ballDirX;
			}
		}
		repaint();
	}
	public void keyTyped(KeyEvent e){}
	public void keyPressed(KeyEvent e){
		if(e.getKeyCode() == KeyEvent.VK_RIGHT){
			if(playerPosX>=600){
				playerPosX = 600;
			}
			else {
				moveRight();
			}
		}
		if(e.getKeyCode() == KeyEvent.VK_LEFT){
			if(playerPosX < 10){
				playerPosX = 10;
			}
			else{
				moveLeft();
			}
		}
		if(e.getKeyCode() == KeyEvent.VK_ENTER){
			if(!play) {
				play = true;
				ballPosX = 120;
				ballPosY = 350;
				ballDirX = -1;
				ballDirY = -2;
				
				playerPosX = 310;
				score = 0;
				totBricks = 21;
				map = new MapGenerator(3,7 );
				repaint();
			}
		}
	}
	public void keyReleased(KeyEvent e){}
	public void moveRight(){
		play = true;
		playerPosX += 20;
	}
	public void moveLeft(){
		play = true;
		playerPosX -= 20;
	}

}
