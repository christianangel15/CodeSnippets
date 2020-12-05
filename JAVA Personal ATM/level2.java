
// package PERSONALATM;
import java.util.Scanner;

public class level2 {
	public static void main(String args[]) {
		double Chqbalance = 0;
		double balance = 0;
		double withdraw;
		double deposit;
		do {
			Scanner scan = new Scanner(System.in);
			System.out.println("Account checking or saving: c or s ");
			char acc = scan.next().charAt(0);
			if (acc != 'c' && acc != 's') {
				System.out.println("Please Enter Valid Input");
				break;
			}
			System.out.println("select: w or d ");
			char in = scan.next().charAt(0);
			switch (in) {
				case 'd':
					System.out.print("deposit how much?: ");
					deposit = scan.nextInt();
					if (acc == 's') {
						balance = deposit;
						System.out.println("Your balance in Savings is: " + balance);
					} else {
						Chqbalance = deposit;
						System.out.println("Your balance in Checking is: " + Chqbalance);
					}
					break;
				case 'w':
					System.out.println("withdraw how much?: ");
					withdraw = scan.nextInt();
					if (acc == 's') {
						if (balance == 0) {
							System.out.println("Zero Balance can't withdraw. Please deposit first");
						} else if (balance >= withdraw) {
							balance -= withdraw;
							System.out.println("Balance left in saving: " + balance);
						} else {
							System.out.println(" sorry ");
						}
					} else {
						if (Chqbalance == 0) {
							System.out.println("Zero Balance can't withdraw. Please deposit first");
						} else if (Chqbalance >= withdraw) {
							Chqbalance -= withdraw;
							System.out.println("Balance left in checking: " + Chqbalance);
						} else {
							System.out.println(" sorry ");
						}
					}

					break;
				default:
					System.out.print("invalid input");
			}
			System.out.println("again? y or n");
			in = scan.next().charAt(0);
			if (in == 'n') {
				System.out.println("Your Checking balance: " + Chqbalance);
				System.out.println("Your Saving balance: " + balance);
				break;
			}
		} while (true);

	}

}