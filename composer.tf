provider "google" {
 //credentials = "${file(local.service_account_path)}"
 project     = "gcptraining-17042017"
}

variable "region" {
default = "us-central1"
}
variable "zone" {
default = "us-central1-b"
}
variable "ml_composer_name" {
default = "panw-demo-composer"
}
variable "ml_composer_node_count" {
default = 4
}
variable "ml_composer_disk_size" {
default = 50
}
variable "ml_composer_node_machine_type" {
default = "n1-standard-1"
}

resource "google_composer_environment" "airflow_composer" {
  name   = "${var.ml_composer_name}"
  region = "${var.region}"

  config {
    node_count = "${var.ml_composer_node_count}"

    node_config {
      zone         = "${var.zone}"
      machine_type = "${var.ml_composer_node_machine_type}"
      disk_size_gb = "${var.ml_composer_disk_size}"
    }
  }

}

/*
data "null_data_source" "composer_bucket" {
  inputs = {
    ml_composer_gcs = "${substr(google_composer_environment.airflow_ml.config.0.dag_gcs_prefix, 0 , length(google_composer_environment.airflow.config.0.dag_gcs_prefix)-5)}"
  }
}

output "ml_composer_gcs" {
  value = "${substr(google_composer_environment.airflow_ml.config.0.dag_gcs_prefix, 0 , length(google_composer_environment.airflow_ml.config.0.dag_gcs_prefix)-5)}"
}

output "ml_airflow_uri" {
  value = "${google_composer_environment.airflow_ml.config.0.airflow_uri}"
}
*/
