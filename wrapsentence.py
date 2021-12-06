# nput_sentence = "Following up from last week in case my note got lost in your inbox"
# len_s = 20
#
#
# output_sentence = "Following up from\n last week in case my\n note got lost in\n your inbox"



def wrappingsentence(sentence, position):

        space = 0
        result = ""
        counter = 0
        prev = 0


        for i in range(0, len(sentence)):
                if counter == position:
                        if sentence[i] == " ":
                                space = i
                                result = result + sentence[prev: space] + "\\n"
                        else:
                                result = result + sentence[prev: space] + "\\n"

                        prev = space
                        counter = 0

                elif sentence[i] == " ":
                        space = i
                        print("space at ", space)
                        counter += 1

                else:
                        counter += 1

        result = result + sentence[prev: ]
        print(result)


if __name__ == '__main__':

    wrappingsentence("Following up from last week in case my note got lost in your inbox", 10)


