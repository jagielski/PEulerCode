cipherfile = open("p059_cipher.txt")
# cipherlist = [int(val) for val in cipherfile.readline().split(',')]
# cipherresults = open('p059_answers.txt', 'w')
# for a in range(97,123):
    # for b in range(97,123):
        # for c in range(97,123):
            # cipherresults.write(chr(a)+chr(b)+chr(c)+'\n')
            # for i in range(len(cipherlist)):
                # if i%3==0:
                    # cipherresults.write(chr(a^cipherlist[i]))
                # elif i%3==1:
                    # cipherresults.write(chr(b^cipherlist[i]))
                # elif i%3==2:    
                    # cipherresults.write(chr(c^cipherlist[i]))
            # cipherresults.write('\n')
text = "(The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He was with God, and he was God. 2 He was in the beginning with God. 3 He created everything there is. Nothing exists that he didn't make. 4 Life itself was in him, and this life gives light to everyone. 5 The light shines through the darkness, and the darkness can never extinguish it. 6 God sent John the Baptist 7 to tell everyone about the light so that everyone might believe because of his testimony. 8 John himself was not the light; he was only a witness to the light. 9 The one who is the true light, who gives light to everyone, was going to come into the world. 10 But although the world was made through him, the world didn't recognize him when he came. 11 Even in his own land and among his own people, he was not accepted. 12 But to all who believed him and accepted him, he gave the right to become children of God. 13 They are reborn! This is not a physical birth resulting from human passion or plan, this rebirth comes from God.14 So the Word became human and lived here on earth among us. He was full of unfailing love and faithfulness. And we have seen his glory, the glory of the only Son of the Father."
count = 0
for char in text:
    count+=ord(char)
print(count)