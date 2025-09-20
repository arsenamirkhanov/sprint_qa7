import subprocess
import sys
import os
import shutil

def install_dependencies():
    print("Установка зависимостей...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    print("Зависимости успешно установлены")
    print("=" * 50)

def run_tests():
    print("Запуск тестов...")
    print("=" * 50)
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--alluredir=allure_results", "-v"],
        text=True
    )
    return result.returncode

def generate_allure_report():
    print("Генерация Allure отчёта...")
    # если старая папка отчёта есть — удаляем
    if os.path.exists("allure_report"):
        shutil.rmtree("allure_report")
    subprocess.run(["allure", "generate", "allure_results", "-o", "allure_report", "--clean"], check=True)
    print("✅ Отчёт сгенерирован: allure_report/")
    print("=" * 50)

def open_allure_report():
    print("Открытие отчёта в браузере...")
    subprocess.run(["allure", "open", "allure_report"], check=True)

def main():
    print("Запуск проекта тестирования API QA Scooter")
    print("=" * 50)

    install_dependencies()

    test_exit_code = run_tests()

    if test_exit_code == 0:
        print("✅ Все тесты прошли успешно")
    else:
        print(f"❌ Некоторые тесты упали (код {test_exit_code})")

    generate_allure_report()
    open_allure_report()

if __name__ == "__main__":
    main()
