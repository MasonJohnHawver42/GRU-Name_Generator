# GRU-Name_Generator


Using a GRU netwrok and a long list of names I was able to train a model to predict the next letter in a sequence of letters to fit training data names. With this predictive power and some probility the model can generate random names that could plausibly seem to be part of the training data. It acomplishes this by being given a random letter then it predicts the next letter and that prediction is tacked on to what it was given and we feed that right back into the model to get the next letter, and we keep repeating this cycle untill the model finally spits out a '.' for indicate its done and the name is generated (for all the names in the training set I tacked on a '.' at the end of them to signal they were over thats how the model knows to end the sequence).


# How to Use

//todo

# Example Results
(I used collage names as the training data)

Names generated after epoch 0:
  *  a.
  * txrzysslnzyfhytek.
  * itqzegpewy.

Names generated after epoch 25:
  * xaldpia college.
  * liride university.
  * .

Names generated after epoch 50:
  * zazrof catemy cellege.
  * nalifotu university.
  * heverdie college.

Names generated after epoch 75:
  * georgia state college of tadierrystof oramorama.
  * zoreda pareer collegevaltor.
  * radto haubis theolonods college.

Names generated after epoch 100:
  * onte sphonsis academy.
  * ldwesdon technical college.
  * lake ho muniey cchrenchifeseora.

Names generated after epoch 125:
  * oathilorican university.
  * ollawine college.
  * rey baybus college inc and feauth mchenwittingu.

Names generated after epoch 150:
  * asion walle college.
  * vendona state university.
  * **university college.**

Names generated after epoch 175:
  * atlon stmte universitytackfond vallers.
  * atera hosigtal universityitadveenspunegs.
  * rosimen university.

Names generated after epoch 200:
  * arkanse forler college.
  * ortheassan state community college.
  * ortane state community college.

Names generated after epoch 225:
  * ckantal tichl college.
  * yle college.
  * olakla merchioo.

Names generated after epoch 250:
  * emflorida state university.
  * acamato university.
  * arvenn university.

Names generated after epoch 275:
  * **radd coast college.**
  * errgreschers pine coluea.
  * illian university.
