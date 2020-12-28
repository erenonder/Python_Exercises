# import multiprocessing
import time
import concurrent.futures


def do_something(sleep_time):
    print(f'Sleeping {sleep_time} seconds')
    time.sleep(sleep_time)
    return 'Wake up...'


def main():
    start = time.perf_counter()
    # print(start)
    print('main started')

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5 - i for i in range(5)]
        # print(secs)
        results = [executor.submit(do_something, sec) for sec in secs]
        # results = executor.map(do_something, secs)

        # for result in results:
        #     print(result)

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()
    print(f'Finished in {finish-start} seconds')


if __name__ == '__main__':
    main()


# This part below is more manual


# def main():
#     start = time.perf_counter()
#     # print(start)
#     print('main started')

#     for process in processes:
#         process.join()
#     finish = time.perf_counter()
#     print(f'Finished in {finish-start} seconds')


# if __name__ == "__main__":
#     processes = []
#     for _ in range(10):
#         p = multiprocessing.Process(target=do_something, args=[2])
#         p.start()
#         processes.append(p)
#     main()
