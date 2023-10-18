package brickBreaker;

import java.awt.*;

public class MapGenerator {
	public int[][] map;
	public int brickWidth;
	public int brickHeight;
	
	public MapGenerator(int row, int col){
		map = new int[row][col];
		for(int i=0;i<row;i++){
			for(int j=0;j<col;j++){
				//1: not intersected with the ball
				//0: intersected with the ball, not to be displayed
				map[i][j] = 1;
			}
		}
		
		brickWidth = 540/col;
		brickHeight = 150/row;
	}
	public void draw(Graphics2D g){
		for(int i=0;i<map.length;i++){
			for(int j=0;j<map.length;j++){
				if(map[i][j] > 0){
					g.setColor(Color.white);
					g.fillRect(j*brickWidth + 80, i*brickHeight + 50, brickWidth, brickHeight);
//					awRect(j*brickWidth + 80, i*brickHeight + 50, brickWidth, brickHeight);
					g.setStroke(new BasicStroke(3));
					g.setColor(new Color(0x403D39));
					g.drawRect(j*brickWidth + 80, i*brickHeight + 50, brickWidth, brickHeight);
					
				}
				else{
					g.setColor(new Color(0x403D39));
					g.fillRect(j*brickWidth + 80, i*brickHeight + 50, brickWidth, brickHeight);
//					awRect(j*brickWidth + 80, i*brickHeight + 50, brickWidth, brickHeight);
					g.setStroke(new BasicStroke(3));
					g.setColor(new Color(0x403D39));
					g.drawRect(j*brickWidth + 80, i*brickHeight + 50, brickWidth, brickHeight);
				}
			}
		}
	}
	
	public void setBrickVal(int val, int row, int col){
	
	}
	
}
