import csv


class FormDataManager:
    @staticmethod
    def save_to_csv(data):
        with open('data/form_data.csv', 'a', newline='', encoding="UTF-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)

    @staticmethod
    def read_from_csv():
        form_data = []
        with open('data/form_data.csv', 'r', newline='', encoding="UTF-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                form_data.append({
                    'title': row[0],
                    'summary': row[1],
                    'user_article': row[2],
                    'author': row[3],
                    'date': row[4]
                })
        return form_data

    @staticmethod
    def article_exists(title):
        data = FormDataManager.read_from_csv()
        for article in data:
            if article['title'] == title:
                return True
        return False

    @staticmethod
    def add_article(title, summary, user_article, author, date):
        if FormDataManager.article_exists(title):
            return False
        else:
            FormDataManager.save_to_csv([title, summary, user_article, author, date])
            return True

    @staticmethod
    def get_article_author(title):
        data = FormDataManager.read_from_csv()
        for article in data:
            if article['title'] == title:
                return article['author']
        return None

    @staticmethod
    def delete_article(title):
        data = FormDataManager.read_from_csv()
        updated_data = [article for article in data if article['title'] != title]
        with open('data/form_data.csv', 'w', newline='', encoding="UTF-8") as csvfile:
            writer = csv.writer(csvfile)
            for article in updated_data:
                writer.writerow(
                    [article['title'], article['summary'], article['user_article'], article['author'], article['date']])
