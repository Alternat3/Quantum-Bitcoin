import time
from hashlib import sha256
from grovers import mine

class Block:
    blockHash = ''
    nonce = ''
    accuracy = 0

    def __init__(self, senderAddr, recieverAddr, amount, previousBlockHash, blockNumber):
        self.senderAddr = senderAddr
        self.recieverAddr = recieverAddr
        self.amount = amount
        self.previousBlockHash = previousBlockHash
        self.blockNumber = blockNumber
        self.timestamp = time.time()

        prevBlockHashBinary = ''.join(format(ord(i), '08b') for i in previousBlockHash)
        self.nonce = prevBlockHashBinary[-3:]
        counter = 0
        avgaccuracy = 0
        print(chosen_accuracy)
        while(self.accuracy < chosen_accuracy):
            counter = counter + 1
            self.accuracy = mine(self.nonce, type_choice)
            avgaccuracy = avgaccuracy + self.accuracy
            print("Iteration {} Accuracy: {} ".format(counter,self.accuracy))
        print("Final Accuracy: ", self.accuracy)
        print("Iterations = ", counter)
        avgaccuracy = avgaccuracy / counter
        print("Average Accuracy = ", avgaccuracy)

        self.blockHash = previousBlockHash + senderAddr + recieverAddr + amount + str(self.timestamp) + str(self.nonce) + str(self.accuracy)
        self.blockHash = sha256(self.blockHash.encode('utf-8')).hexdigest()



class Blockchain:
    blockchain = []
    def __init__(self):
        if len(self.blockchain) < 1:
            genBlock = Block('Genesis', 'Genesis', '0', '0', 1)
            self.blockchain.append(genBlock)
    
    def addBlock(self, additionalBlock):
        self.blockchain.append(additionalBlock)
    
    def printChain(self):
        print('Block : Blockhash                                                         : Reciever : Sender : Amount : Accuracy')
        for x in range(len(self.blockchain)):
            print(self.blockchain[x].blockNumber, self.blockchain[x].blockHash, ' : ', self.blockchain[x].recieverAddr, ' : ', self.blockchain[x].senderAddr, ' : ', self.blockchain[x].amount, ' : ',self.blockchain[x].accuracy)

def userChoice1(blockchain):

    print("Please input sender address: ")
    sendrAddr = input()
    print("Please input reciever address: ")
    recvAddr = input()
    print("Enter amount: ")
    amount = input()

    chainLength = len(blockchain.blockchain)
    previousBlockNumber = blockchain.blockchain[chainLength - 1].blockNumber
    prevBlockHash = blockchain.blockchain[chainLength - 1].blockHash

    currentBlock = Block(sendrAddr, recvAddr, amount, prevBlockHash, previousBlockNumber + 1)
    blockchain.addBlock(currentBlock)

def main():
    global sim_accuracy
    sim_accuracy = 78.8
    global quantum_accuracy
    quantum_accuracy = 45.5
    global type_choice

    print("Please choose (1) simulator or (2) real quantum version: ")
    type_choice = input()
    match type_choice:
        case "1":
            global chosen_accuracy
            chosen_accuracy = sim_accuracy
        case "2":
            chosen_accuracy = quantum_accuracy

    blockchain = Blockchain()
    
    while(1):
        print("Choose option: ")
        print("1. Add new block to chain.")
        print("2. Display blocks on current blockchain.")
        choice = input()
    
        match choice:
            case "1":
                userChoice1(blockchain)
            case "2":
                blockchain.printChain()
            case _:
                print("Invalid choice")
    
if __name__ == "__main__":
    main()