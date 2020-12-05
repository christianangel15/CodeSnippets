import java.util.Scanner;
import java.util.Arrays;

public class level3 {
	public static void main(String args[]) {
		double Chqbalance = 0;
		double balance = 0;
		int withdraw;
		int deposit;
		int[] arrS = {};
		int[] arrSW = {};
		int[] arrSD = {};
		int[] arrC = {};
		int[] arrCW = {};
		int[] arrCD = {};
		do {
			int arrST = arrSW.length + arrSD.length;
			int arrCT = arrCW.length + arrCD.length;
			if (arrST > 4) {
				System.out.println("Maximum Transaction limit reached");
				break;
			} else if (arrCT > 4) {
				System.out.println("Maximum Transaction limit reached");
				break;
			}
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
						balance += deposit;
						System.out.println("Your balance in Savings is: " + balance);
						if (deposit != 0) {
							arrSD = Arrays.copyOf(arrSD, arrSD.length + 1);
							arrSD[arrSD.length - 1] = deposit;
						}
					} else {
						Chqbalance += deposit;
						System.out.println("Your balance in Checking is: " + Chqbalance);
						if (deposit != 0) {
							arrCD = Arrays.copyOf(arrCD, arrCD.length + 1);
							arrCD[arrCD.length - 1] = deposit;
						}
					}
					break;
				case 'w':
					if (acc == 's') {
						if (balance == 0) {
							System.out.println("Zero Balance can't withdraw. Please deposit first");
							break;
						}
						System.out.println("withdraw how much?: ");
						withdraw = scan.nextInt();
						if (balance >= withdraw) {
							balance -= withdraw;
							System.out.println("Balance left in saving: " + balance);
							if (withdraw != 0) {
								arrSW = Arrays.copyOf(arrSW, arrSW.length + 1);
								arrSW[arrSW.length - 1] = withdraw;
							}
						} else {
							System.out.println(" sorry ");
						}
					} else {
						if (Chqbalance == 0) {
							System.out.println("Zero Balance can't withdraw. Please deposit first");
							break;
						}
						System.out.println("withdraw how much?: ");
						withdraw = scan.nextInt();
						if (Chqbalance >= withdraw) {
							Chqbalance -= withdraw;
							System.out.println("Balance left in checking: " + Chqbalance);
							if (withdraw != 0) {
								arrCW = Arrays.copyOf(arrCW, arrCW.length + 1);
								arrCW[arrCW.length - 1] = withdraw;
							}
						} else {
							System.out.println(" sorry ");
						}
					}

					break;
				default:
					System.out.print("invalid input");
			}
			System.out.println("Another Transaction? y or n");
			in = scan.next().charAt(0);
			if (in == 'n') {
				int sum = 0;
				int sum1 = 0;
				System.out.println("Your Saving balance history");
				System.out.println("" + balance);
				for (int num : arrSW) {
					sum = sum + num;
				}
				System.out.println("-" + sum);
				System.out.println("Your Checking balance history");
				System.out.println("" + Chqbalance);
				for (int num1 : arrCW) {
					sum1 = sum1 + num1;
				}
				System.out.println("-" + sum1);
				break;
			}
		} while (true);

	}

}