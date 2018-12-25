import java.util.*;
import java.io.*;

class Bot implements Comparable<Bot> {

	public long x,y,z,r;

	public Bot(long x, long y, long z, long r) {
		this.x = x;
		this.y = y;
		this.z = z;
		this.r = r;
	}

	public boolean inRange(long x, long y, long z) {
		return Math.abs(x-this.x)+Math.abs(y-this.y)+Math.abs(z-this.z) <= r;
	}

	public int compareTo(Bot other) {
		return (this.x+this.y+this.z) > (other.x+other.y+other.z) ? 1 : -1;
	}

}

public class Advent2018_23 {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner s = new Scanner(new File("input.txt"));
		ArrayList<Bot> bots = new ArrayList<Bot>();
		while (s.hasNext()) {
			String line = s.nextLine();
			bots.add(new Bot(Integer.parseInt(line.split("<|,|=|>")[2]),Integer.parseInt(line.split("<|,|=|>")[3]),Integer.parseInt(line.split("<|,|=|>")[4]),Integer.parseInt(line.split("<|,|=|>")[7]))); // stolen
		}
		// we now have a list of bots
		long ix,ax,iy,ay,iz,az,window;
		ix = -200000000;
		ax = 200000000;
		iy = -200000000;
		ay = 200000000;
		iz = -200000000;
		az = 200000000;
		window = 4000000;
		Bot maxbot = new Bot(0, 0, 0, 0);
		int maxn = 0;

		while (window > 0) {

			maxn = 0;
			maxbot = new Bot(ax, ay, az, 0);

			for (long x = ix; x < ax; x += window) {
				for (long y = iy; y < ay; y += window) {
					for (long z = iz; z < az; z += window) {
						int k = nInRange(x, y, z, bots);
						if (k > maxn || k == maxn && maxbot.compareTo(new Bot(x, y, z, 0)) > 0) {
							maxn = k;
							maxbot = new Bot(x, y, z, 0);
						}
					}
				}
			}
			System.out.println(maxbot.x+", "+maxbot.y+", "+maxbot.z+"; n = "+maxn);
			
			window /= 2;
			ix = (ix+maxbot.x)/2;
			ax = (ax+maxbot.x)/2;
			iy = (iy+maxbot.y)/2;
			ay = (ay+maxbot.y)/2;
			iz = (iz+maxbot.z)/2;
			az = (az+maxbot.z)/2;

		}

		System.out.println("distance = "+(maxbot.x+maxbot.y+maxbot.z));
	}

	public static int nInRange(long x, long y, long z, List<Bot> bots) {
		int c = 0;
		for (Bot b : bots) {
			if (b.inRange(x, y, z)) c++;
		}
		return c;
	}

}