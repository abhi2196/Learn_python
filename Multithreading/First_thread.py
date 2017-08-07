import threading


def f(id):
	print 'Inside Thread Function Called by Thread ID: %d' % (id)
	return

if __name__ == '__main__':
	for i in range(3):
		t = threading.Thread(target=f, args=(i,))
		t.start()

