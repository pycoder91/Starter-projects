import java.util.Scanner;
import java.util.Random;

public class HangmanGame {
    private static final String[] words = {"java", "hangman", "programming", "computer", "games", "player", "guess", "word"};
    private static final Random random = new Random();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String secretWord = words[random.nextInt(words.length)];
        int wordLength = secretWord.length();
        int attempts = 6;
        StringBuilder guessedLetters = new StringBuilder();

        System.out.println("Welcome to Hangman!");
        System.out.println("The word contains " + wordLength + " letters.");
        System.out.println("You have 6 attempts to guess the word.");

        while (attempts > 0) {
            StringBuilder display = new StringBuilder();
            for (int i = 0; i < wordLength; i++) {
                char letter = secretWord.charAt(i);
                if (guessedLetters.toString().contains(String.valueOf(letter))) {
                    display.append(letter).append(" ");
                } else {
                    display.append("_ ");
                }
            }
            System.out.println(display);

            if (!display.toString().contains("_")) {
                System.out.println("Congratulations! You've guessed the word.");
                break;
            }

            System.out.print("Guess a letter: ");
            String guess = scanner.nextLine().toLowerCase();

            if (guess.length() != 1 || !Character.isLetter(guess.charAt(0))) {
                System.out.println("Please enter a single letter.");
                continue;
            }

            if (guessedLetters.toString().contains(guess)) {
                System.out.println("You've already guessed that letter. Try a different one.");
                continue;
            }

            guessedLetters.append(guess);

            if (!secretWord.contains(guess)) {
                attempts--;
                System.out.println("Sorry, '" + guess + "' is not in the word. Attempts left: " + attempts);
            } else {
                System.out.println("Good guess!");
            }
        }

        if (!guessedLetters.toString().contains("_")) {
            System.out.println("Sorry, you've run out of attempts. The word was: " + secretWord);
        }
    }
}
