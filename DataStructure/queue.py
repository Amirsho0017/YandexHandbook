# FIFO, pop, push(put), top([-1])
import _queue

values = _queue.SimpleQueue()
# Добавление элементов в очередь
values.put(1)
values.put(2)
values.put(3)

# Извлечение элементов из очереди
print(values.get())  # Выводит 1
print(values)  # Выводит 2

