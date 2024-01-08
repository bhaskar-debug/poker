# poker

## Relevant Information

Each record is an example of a hand consisting of five playing
cards drawn from a standard deck of 52. Each card is described
using two attributes (suit and rank), for a total of 10 predictive
attributes. There is one Class attribute that describes the
**Poker Hand** The order of cards is important, which is why there are 480 possible Royal Flush hands as compared to 4 (one for each suit explained in more detail below).

Number of Attributes: 10 predictive attributes, 1 goal attribute

## Attribute Information

   1) S1 **Suit of card #1**
      Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}

   2) C1 **Rank of card #1**
      Numerical (1-13) representing (Ace, 2, 3, ... , Queen, King)

   3) S2 **Suit of card #2**
      Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}

   4) C2 **Rank of card #2**
      Numerical (1-13) representing (Ace, 2, 3, ... , Queen, King)

   5) S3 **Suit of card #3**
      Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}

   6) C3 **Rank of card #3**
      Numerical (1-13) representing (Ace, 2, 3, ... , Queen, King)

   7) S4 **Suit of card #4**
      Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}

   8) C4 **Rank of card #4**
      Numerical (1-13) representing (Ace, 2, 3, ... , Queen, King)

   9) S5 **Suit of card #5**
      Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}

   10) C5 **Rank of card #5**
      Numerical (1-13) representing (Ace, 2, 3, ... , Queen, King)

   11) CLASS **Poker Hand**
      Ordinal (0-9)

      0: Nothing in hand; not a recognized poker hand 
      1: One pair; one pair of equal ranks within five cards
      2: Two pairs; two pairs of equal ranks within five cards
      3: Three of a kind; three equal ranks within five cards
      4: Straight; five cards, sequentially ranked with no gaps
      5: Flush; five cards with the same suit
      6: Full house; pair + different rank three of a kind
      7: Four of a kind; four equal ranks within five cards
      8: Straight flush; straight + flush
      9: Royal flush; {Ace, King, Queen, Jack, Ten} + flush

## Class Distribution

### Testing set

The value inside parenthesis indicates the representation within the test set as compared to the entire domain. 1.0 would be perfect representation, while <1.0 are under-represented and >1.0 are over-represented.

      0: Nothing in hand, 501209 instances,(1.000063)
      1: One pair, 422498 instances,(0.999832)
      2: Two pairs, 47622 instances, (1.001746)
      3: Three of a kind, 21121 instances, (0.999647)
      4: Straight, 3885 instances, (0.989897)
      5: Flush, 1996 instances, (1.015569)
      6: Full house, 1424 instances, (0.988491)
      7: Four of a kind, 230 instances, (0.957934)
      8: Straight flush, 12 instances, (0.866426)
      9: Royal flush, 3 instances, (1.948052)

      Total of one million instances in a domain of 311,875,200.

## Google colab

### Phase 1: Poker hand Prediction Task

- Download this repository https://drive.google.com/drive/folders/1nRhbyhyzSSwsjwuXeJZ84FoQE_TtVxBE?usp=drive_link as a zip file.
- After unzipping copy the folder poker to the Google Drive of the Google account which has access to the Google Colab.
- Open this file `poker-hand-prediction.ipynb` by double-clicking it will open in Google Colab.
- After opening in Google Colab on the right side you will see RAM and Disk. Click on it, it will open resources.
- Click on the `Change Runtime type` button to change the runtime at down.
- Make sure to click on the TPU and High RAM as they are available in the `Colab Pro+` account, it will speed up the training time.
- Now run the notebook cells one by one.
- `Google Drive mount` step will automatically mount the Google Drive to Colab, allowing you to save all the files back to the same location and model and everything in the Google Drive.(Select the Google drive account previously where colab pro plus account is and al the data saved previously and allow them in every step)
- Proceed to do step-by-step instructions in the notebook cells.
- Goto folder `sample_player` you will see the folder `utils_teamACN` rename it to your team name like `utils_yourteamname`.
- The whole cell in preprocess TODO step, copy it in your `sample_player/utils_yourteamname/preprocess.py` for future use of preprocess step in prediction.

### Phase 2: Poker Pre flop strategy and flop strategy creation using the prediction made in phase 1

- Open this file `poker-strategy.ipynb` by double-clicking it will open in Google Colab.
- After opening the file same change the runtime as Phase 1 and follow the instructions in the notebook.
- The whole cell in pre_flop TODO step, copy it in your `sample_player/utils_yourteamname/pre_flop_strategy.py` for use in poker game showdown.
- The whole cell in flop TODO step, copy it in your `sample_player/utils_yourteamname/flop_strategy.py` for use in poker game showdown.
- At the end of the completion of the task please share the Google Drive location of your task.
