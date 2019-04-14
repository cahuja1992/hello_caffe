#include "classifier.hh"

int main(int argc, char** argv) {
	std::cout<<"..... Hello Caffe Classification ......\n";

  if (argc != 6) {
    std::cerr << "Usage: " << argv[0]
              << " deploy.prototxt network.caffemodel"
              << " mean.binaryproto labels.txt img.jpg" << std::endl;
    return 1;
  }

  ::google::InitGoogleLogging(argv[0]);

  string model_file   = argv[1];
  string trained_file = argv[2];
  string mean_file    = argv[3];
  string label_file   = argv[4];
  string file = argv[5];

  Classifier classifier(model_file, trained_file, mean_file, label_file);

  cv::Mat img = cv::imread(file, -1);
  CHECK(!img.empty()) << "Unable to decode image " << file;
  std::vector<Prediction> predictions = classifier.Classify(img);

  for (size_t i = 0; i < predictions.size(); ++i) {
    Prediction p = predictions[i];
    std::cout << "\"confidence\": " << std::fixed << std::setprecision(4) << p.second << ", \"label\": \"" << p.first << "\" }" << std::endl;
  }

  return 0;
}
