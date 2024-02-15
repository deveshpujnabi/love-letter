def main():
  love_letter = """
Hey {recipient},
life with you seems like a non-stop comedy show, and I'm ready for a lifetime subscription. 
How about we upgrade this friendship to a full-blown romance?
What do you say we make our own sitcom and call it "Love and Laughter"? 
Ready for this hilarious adventure together?

Your Lover,
{sender}
"""

  recipient = input("Enter your name: ")
  sender = input("Enter sender name: ")

  love_letter = love_letter.format(recipient=recipient, sender=sender)

  print(love_letter)

  while True:
      response = input("Would you like to marry me? (yes/no): ").lower()

      if response == "yes":
          print("Congratulations! I'm so happy for you both.")
          break
      elif response == "no":
          print("I'm sorry to hear that. I hope you find the happiness you're looking for.")
          break
      else:
          print("Invalid response. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
  main()