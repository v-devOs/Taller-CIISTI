import eel

from utils.database.exposer import ExposerDB


def main():
  eel.init('web')
  eel.start('index.html', mode='edge')

  # exposer = ExposerDB

if __name__ == '__main__':
  main()