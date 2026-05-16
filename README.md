[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kOqwghv0)
# ML Project: Определение съедобности грибов

**Студент:** Воронцова Дарья Николаевна / dnvorontsova@edu.hse.ru

**Группа**: БИВ233


## Оглавление

1. [Описание задачи](#описание-задачи)
2. [Структура репозитория](#структура-репозитория)
3. [Запуски](#запуск)
4. [Данные](#данные)
5. [Результаты](#результаты)
6. [Отчет](#отчет)


## Описание задачи

**Задача:** бинарная классификация грибов по морфологическим признакам.

**Датасет:** Secondary Mushroom Dataset, Kaggle: <https://www.kaggle.com/datasets/joebeachcapital/secondary-mushroom-dataset/data>

**Целевая переменная:** `class`, где `e` - съедобный гриб, `p` - ядовитый или не рекомендованный к употреблению.

**Основная метрика:** F1-score. Дополнительно считаются accuracy, precision, recall и ROC-AUC.

## Структура проекта

```text
.
├── data
│   ├── raw                  # исходные CSV и описания датасета
│   └── processed            # train/val/test после подготовки
├── models                   # сохраненные модели
├── notebooks
│   ├── 01_data_preparation.ipynb
│   ├── 02_baseline.ipynb
│   └── 03_modeling_experiments.ipynb
├── presentation             # Презентация для защиты
├── report
│   ├── report.md            # Финальный отчет
│   ├── experiment_results.csv
│   └── final_test_metrics.json
├── src
├── tests                    # Тесты пайплайна
├── Dockerfile
├── pytest.ini
├── requirements.txt
└── README.md
```

## Запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/hsemlcourse/hseml-group-project-daryavorontsova.git
cd hseml-group-project-daryavorontsova

# 2. Создать виртуальное окружение
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

# 3. Установить зависимости
pip install -r requirements.txt
```

Проверки качества:

```bash
ruff check src tests --line-length 120
flake8 src tests
pytest
```

Запуск в Docker:

```bash
docker build -t mushroom-edibility .
docker run --rm mushroom-edibility
```

## Данные

Локальные исходные файлы находятся в `data/raw`. Основной файл для моделирования: `data/raw/secondary_data.csv`.

После выполнения `01_data_preparation.ipynb` создаются:

- `data/processed/train.csv`
- `data/processed/val.csv`
- `data/processed/test.csv`

## Результаты

### Baseline

Baseline-модель находится в `notebooks/02_baseline.ipynb`: `LogisticRegression` с `OneHotEncoder` для категориальных признаков и `StandardScaler` для числовых. Ручной feature engineering в baseline не используется.

Test-результаты baseline:

| Accuracy | F1 | Precision | Recall | ROC-AUC |
| ---: | ---: | ---: | ---: | ---: |
| 0.8594 | 0.8437 | 0.8370 | 0.8504 | 0.9335 |

### Моделирование и эксперименты

Основные эксперименты находятся в `notebooks/03_modeling_experiments.ipynb`. Были проверены логистическая регрессия, дерево решений, RandomForest, ExtraTrees, GradientBoosting, AdaBoost, модели с `TruncatedSVD`, KNN и soft-voting ensemble.

Полная таблица экспериментов сохранена в `report/experiment_results.csv`.

Текущие test-результаты финальной модели:

| Accuracy | F1 | Precision | Recall | ROC-AUC | Dangerous errors |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0.9998 | 0.9998 | 0.9995 | 1.0000 | 1.0000 | 2 |

`dangerous_errors` — число случаев, когда ядовитый / не рекомендованный гриб был ошибочно предсказан как съедобный.

## Отчет

Финальный отчет: [report/report.md](report/report.md).

Отчетные артефакты:

- [report/experiment_results.csv](report/experiment_results.csv)
- [report/final_test_metrics.json](report/final_test_metrics.json)
