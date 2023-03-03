#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QProcess>
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->comboBox->addItem("md5");
    ui->comboBox->addItem("sha1");
    ui->comboBox->addItem("sha224");
    ui->comboBox->addItem("sha256");
    ui->comboBox->addItem("sha384");
    ui->comboBox->addItem("sha512");
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    QString text = ui->lineEdit_input->text();
    QString command = "python3 /home/vance/Documents/projact/hash-sky/hash-sky/main.py ";
    command += ui->comboBox->currentText();
    command += " ";
    command += text;

    QProcess p;
    QStringList params;
    p.start(command);
    p.waitForFinished(-1);

    QString p_stdout = p.readAll();
    ui->textEdit_output->setText(p_stdout);
}

void MainWindow::on_pushButton_2_clicked()
{
   ui->textEdit_output->selectAll();
   ui->textEdit_output->copy();
}
