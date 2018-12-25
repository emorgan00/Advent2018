class Marble {

	public Marble previous,next; // I'm going to hell for making these public
	public long value;

	public Marble(long value, Marble previous, Marble next) {
		this.value = value;
		this.next = next;
		this.previous = previous;
	}

	public Marble get_next(int n) { // returns the marble n spots clockwise from this marble
		if (n == 0) return this;
		else return this.next.get_next(n-1);
	}

	public Marble get_previous(int n) { // returns the marble n spots counter-clockwise from this marble
		if (n == 0) return this;
		else return this.previous.get_previous(n-1);
	}

}

public class advent2018_09 {

	public static void main(String[] args) {
		Marble current = new Marble(0,null,null);
		current.next = current;
		current.previous = current; // we now have a node which links to itself in both directions

		int p = 479; // number of players
		int l = 7103500; // value of largest number

		long[] scores = new long[p]; // all are 0 by default
		int counter = 0; // value of next marble to be added

		Marble before,after; // we will use these later

		while (counter < l+1) {
			if (counter%23 == 0) { // if we are a multiple of 23...

				// before and after are the nodes 8 counter-clockwise and 6 counter-clockwise:
				after = current.get_previous(6);
				before = after.get_previous(2);

				// adding the 7-counter-clockwise marble to a player's score:
				scores[counter%p] += counter; // adding the marble that would have been added.
				scores[counter%p] += after.previous.value;

				// updating the relevant marbles to link to the correct other marbles:
				before.next = after;
				after.previous = before; // eliminating all trace of the removed marble.
				current = after; // the new current marble is the marble which appeared after the removed marble.
			} else { // if we aren't a multiple of 23...

				// before and after are the node 1 clockwise and 2 clockwise
				before = current.next;
				after = before.next;
				current = new Marble(counter,before,after); // sandwiching a new marble between before and after with value = counter

				// updating the relevant marbles to link to the correct other marbles:
				before.next = current;
				after.previous = current;
			}
			counter++;
		}
		// simply getting the largest number in scores[]:
		long max = 0;
		for (long score : scores) if (score > max) max = score;
		System.out.println("Winning score: "+max);
	}

}