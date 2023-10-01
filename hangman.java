import java.util.Scanner;

public class HangmanGame {
    private static final String[] WORDS = { "java", "python", "programming", "hangman", "computer" };
    private static final int MAX_TRIES = 6;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean playAgain = true;

        while (playAgain) {
            String secretWord = selectRandomWord(WORDS);
            String guessedWord = initializeGuessedWord(secretWord);
            int tries = 0;
            boolean isGameOver = false;

            System.out.println("Welcome to Hangman!");
            System.out.println("Guess the word:");

            while (!isGameOver) {
                displayHangman(tries);
                displayWord(guessedWord);

                char guess = getGuess(scanner);

                if (secretWord.contains(String.valueOf(guess))) {
                    guessedWord = updateGuessedWord(secretWord, guessedWord, guess);
                } else {
                    tries++;
                    System.out.println("Incorrect guess. Tries left: " + (MAX_TRIES - tries));
                }

                if (guessedWord.equals(secretWord) || tries >= MAX_TRIES) {
                    isGameOver = true;
                    if (guessedWord.equals(secretWord)) {
                        System.out.println("Congratulations! You guessed the word: " + secretWord);
                    } else {
                        System.out.println("Game over! The word was: " + secretWord);
                    }
                }
            }

            System.out.print("Play again? (yes/no): ");
            String playAgainInput = scanner.next().toLowerCase();
            playAgain = playAgainInput.equals("yes");
        }

        System.out.println("Thanks for playing Hangman!");
        scanner.close();
    }

    private static String selectRandomWord(String[] words) {
        int randomIndex = (int) (Math.random() * words.length);
        return words[randomIndex];
    }

    private static String initializeGuessedWord(String word) {
        StringBuilder builder = new StringBuilder(word.length());
        for (int i = 0; i < word.length(); i++) {
            builder.append("_");
        }
        return builder.toString();
    }

    private static void displayHangman(int tries) {
        // Implement hangman drawing here
    }

    private static void displayWord(String word) {
        System.out.println("Word: " + word);
    }

    private static char getGuess(Scanner scanner) {
        System.out.print("Enter a letter: ");
        String input = scanner.next().toLowerCase();
        if (input.length() != 1 || !Character.isLetter(input.charAt(0))) {
            System.out.println("Invalid input. Please enter a single letter.");
            return getGuess(scanner);
        }
        return input.charAt(0);
    }

    private static String updateGuessedWord(String secretWord, String guessedWord, char guess) {
        StringBuilder builder = new StringBuilder(guessedWord);
        for (int i = 0; i < secretWord.length(); i++) {
            if (secretWord.charAt(i) == guess) {
                builder.setCharAt(i, guess);
            }
        }
        return builder.toString();
    }
}
