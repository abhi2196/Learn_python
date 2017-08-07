import threading


def f():
	print 'Inside Thread Function'
	return

if __name__ == '__main__':
	for i in range(3):
		t = threading.Thread(target=f)
		t.start()

