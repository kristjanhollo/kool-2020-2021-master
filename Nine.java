package Nine;

// to do refactor
// OOP
// add bank system
// add more games
// Stop writing spaghetti



import java.util.Scanner;


public class Nine {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int dice = (int) (Math.random() * 6 + 1);           // Players first die
        int diceTwo = (int) (Math.random() * 6 + 1);        // Players second die
        int cpuDice = (int) (Math.random() * 6 + 1);        // cpu first die
        int cpuDiceTwo = (int) (Math.random() * 6 + 1);     // cpu second die

        System.out.println("֍֍֍֍֍ ♠♣♥♦ ֍֍֍֍֍ \n" +
                "♠ GAME OF NINE ♠ \n" +
                "֍֍֍֍֍ ♠♣♥♦ ֍֍֍֍֍ \n" +
                "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ ");

        System.out.println("\n\nWould you like to know the rules? (Y/N)");

        String rules = scanner.nextLine();
        rules = rules.toUpperCase();

        if (rules.equals("Y")) {
            System.out.println("\t\t\t\t\tWelcome to 'Game of Nine'\n" +
                    "\tPoint of the game is to get closest to 9 with two rolls of die\n" +
                    "\tIf you go over 10, you are bust and automatically lose\n" +
                    "\tSame rules apply for your opponent 'Mr. Bond'\n");
        }

        System.out.println("Are you read to play? (Y/N)");

        String start = scanner.nextLine();
        start = start.toUpperCase();

//        Player side of program
//        If input Y , program starts
//        If input N , program ends

        if (start.equals("Y")) {
            System.out.printf("You rolled a %d ", dice);
            System.out.println("\nWould you like to roll again? (Y/N)");

            String contPlaying = scanner.nextLine();
            contPlaying = contPlaying.toUpperCase();                  // convert answer to upper, lower works as well

            if (contPlaying.equals("Y")) {
                dice += diceTwo;
                System.out.printf("You rolled a %d and in total you have %d", diceTwo, dice);
            } else if (contPlaying.equals("N")) {
                System.out.printf("You end up with %d points", dice);
            }
        } else {
            System.out.println("Good bye!");
        }

//      Computer side of program


        if (start.equals("N")) {
        } else if (start.equals("Y")) {
            System.out.printf("\nMr.Bond rolled %d ", cpuDice);
            if (cpuDice > dice) {
                System.out.printf("\nMr.Bond ends up with %d ", cpuDice);
            } else if (cpuDice <= 4) {
                System.out.printf("\nMr.Bond rolls again %d", cpuDiceTwo);
                cpuDice += cpuDiceTwo;
                System.out.printf("\nMr.Bond ends up with %d", cpuDice);
            }

//      Check who won

            if (dice > 9) {
                System.out.println("\nYou bust and lose");
            } else if (cpuDice > 9) {
                System.out.println("\nMr.Bond goes bust and you win");
            } else if (dice > cpuDice) {
                System.out.println("\nCongratulations you win!");
            } else {
                System.out.println("\nSadly you lose!");
            }

        }
    }
}