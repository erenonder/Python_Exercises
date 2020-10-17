import bs4
import requests
import numpy as np
from matplotlib import pyplot as plt


class Graph():
    def __init__(self):
        pass

    def __autolabel(self, rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            plt.annotate('{}'.format(height),
                         xy=(rect.get_x() + rect.get_width() / 2, height),
                         xytext=(0, 3),  # 3 points vertical offset
                         textcoords="offset points",
                         ha='center', va='bottom')

    def show_graph(self, episodes, ratings, episode_count=10):

        labels = []

        for episode in range(1, episode_count + 1):
            labels.append(f'Episode {episode}')

        # print(labels)

        season1 = ratings[0]
        season2 = ratings[1]
        season3 = ratings[2]

        x = np.arange(len(labels))  # the label locations
        width = 0.25  # the width of the bars

        # fig, ax = plt.subplots()
        # print(season1)
        rects1 = plt.bar(x - width, season1, width=width, label='Season 1')
        rects2 = plt.bar(x, season2, width=width, label='Season 2')
        rects3 = plt.bar(x + width, season3, width=width, label='Season 3')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        plt.ylabel('Rating')
        plt.title('Fargo')
        plt.xlabel('Episodes')
        plt.xticks(ticks=x, labels=labels)

        plt.legend()

        self.__autolabel(rects1)
        self.__autolabel(rects2)
        self.__autolabel(rects3)

        plt.tight_layout()

        plt.show()


class IMDB():
    def __init__(self, movie_id):

        self.movie_id = movie_id

        self.season_episode_dict = {}
        self.season_count = self.check_number_of_seasons()

        for season in range(0, self.season_count):
            episode_count = self.check_number_of_episodes(season + 1)
            # print(f'Onder episode_count: {episode_count}')
            if f'season{season+1}' not in self.season_episode_dict.keys():
                self.season_episode_dict[f'season{season+1}'] = episode_count

        # print(self.season_episode_dict)

        # print(
            # f'season count: {self.season_count} episode_count: {episode_count}')

        self.episodes = np.zeros((self.season_count, episode_count))
        self.data = np.zeros((self.season_count, episode_count))

    def check_number_of_episodes(self, season=1):
        web_page = f"https://www.imdb.com/title/tt{self.movie_id}/episodes?season={season}"
        response = requests.get(web_page)
        episode_count = 0

        if response.status_code == requests.codes.ok:

            soup = bs4.BeautifulSoup(response.content, 'lxml')

            for episode in range(1, 11):
                css_selector_title = f"#episodes_content > div.clear > div.list.detail.eplist > div:nth-child({episode}) > div.info > strong > a"
                title = soup.select(css_selector_title)

                if len(title) == 0:
                    break
                else:
                    episode_count += 1

                # print(f'title: {title} episode_count: {episode_count}')

        return episode_count

    def check_number_of_seasons(self):

        season_count = 0

        web_page = f"https://www.imdb.com/title/tt{self.movie_id}"
        response = requests.get(web_page)

        if response.status_code == requests.codes.ok:

            soup = bs4.BeautifulSoup(response.content, 'lxml')

            for season in range(1, 10):
                css_selector_season = f"#title-episode-widget > div > div:nth-child(4) > a:nth-child({season})"
                title = soup.select(css_selector_season)

                if len(title) == 0:
                    break
                else:
                    season_count += 1

        return season_count

    def grab_rates_per_season(self):
        for season in range(1, self.season_count):

            web_page = f"https://www.imdb.com/title/tt{self.movie_id}/episodes?season={season}"
            response = requests.get(web_page)

            if response.status_code == requests.codes.ok:

                soup = bs4.BeautifulSoup(response.content, 'lxml')

                print(f'\nSeason {season}')
                print('------------------')
                for episode in range(1, 11):
                    self.episodes[season - 1][episode - 1] = episode
                    css_selector_title = f"#episodes_content > div.clear > div.list.detail.eplist > div:nth-child({episode}) > div.info > strong > a"
                    css_selector_rating = f"#episodes_content > div.clear > div.list.detail.eplist > div:nth-child({episode}) > div.info > div.ipl-rating-widget > div.ipl-rating-star.small > span.ipl-rating-star__rating"
                    css_selector_vote = f"#episodes_content > div.clear > div.list.detail.eplist > div:nth-child({episode}) > div.info > div.ipl-rating-widget > div.ipl-rating-star.small > span.ipl-rating-star__total-votes"
                    rating = soup.select(css_selector_rating)
                    title = soup.select(css_selector_title)
                    vote_count = soup.select(css_selector_vote)

                    if len(rating) != 0:
                        print(
                            f"Episode {episode:02} {title[0].text:40} vote: {vote_count[0].text:8} rating: {rating[0].text}")
                        self.data[season - 1][episode -
                                              1] = (float(rating[0].text))

        return self.episodes, self.data


if __name__ == '__main__':
    imdb = IMDB('2802850')
    graph = Graph()

    # print(f's: {imdb.season_count} ep: {imdb.episode_count}')

    episodes, data = imdb.grab_rates_per_season()

    # print(episodes)

    # print(data)

    graph.show_graph(episodes, data)
