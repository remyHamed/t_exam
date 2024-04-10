# t_exam

class Referee:
	def __init__(self, queue):
		self.queue = queue

	def run(self):# il initie le jeu en lançant un nombre entre 10000 et 100000 à un joueur (au hasard)
		number = random.randint(10000, 100000)
		print(f"Number is {number}")
		self.queue.push(number)
		while True:
			number = self.queue.pop()
			if number == 1:
				break
			if number % 2 == 0:
				self.queue.push(number // 2)
			else:
				self.queue.push((3 * number + 1) // 2)

if __name__ == "__main__":
	q = Queue()
	players = [Player("J1", q), Player("J2", q)]
	ref = Referee(q)
	threads = [Thread(target=ref.run)]
	for p in players:
		threads.append(Thread(target=p.run))
	for t in threads:
		t.start()
	for t in threads:
		t.join()

	print("finished....")