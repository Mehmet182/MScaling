
from sdks.novavision.src.helper.package import PackageHelper
from components.MScaling.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, MScaleExecutorOutputs, MScaleExecutorResponse, MScaleExecutor, OutputImage
from components.MScaling.src.models.PackageModel import HoughCircleExecutorOutputs,HoughCircleExecutorResponse ,HoughCircleExecutor
from components.MScaling.src.models.PackageModel import GaussianBlurExecutorOutputs , GaussianBlurExecutorResponse,GaussianBlurExecutor



def build_response_Mscaling(context):
    outputImage = OutputImage(value=context.image)

    mScalingExecutor = MScaleExecutorOutputs(outputImage=outputImage)

    mScaleExecutorResponse = MScaleExecutorResponse(outputs=mScalingExecutor)

    mScaleExecutor = MScaleExecutor(value=mScaleExecutorResponse)

    executor = ConfigExecutor(value=mScaleExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel



def build_response_Blur(context):
    outputImage = OutputImage(value=context.image)

    gaussianBlurExecutorOutputs = GaussianBlurExecutorOutputs(outputImage=outputImage)

    gaussianBlurExecutorResponse = GaussianBlurExecutorResponse(outputs=gaussianBlurExecutorOutputs)

    gaussianBlurExecutor = GaussianBlurExecutor(value=gaussianBlurExecutorResponse)

    executor = ConfigExecutor(value=gaussianBlurExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel




def build_response_Circle(context):
    outputImage = OutputImage(value=context.image)

    gaussianBlurExecutorOutputs = HoughCircleExecutorOutputs(outputImage=outputImage)

    houghCircleExecutorResponse = HoughCircleExecutorResponse(outputs=gaussianBlurExecutorOutputs)

    houghCircleExecutor = HoughCircleExecutor(value=houghCircleExecutorResponse)

    executor = ConfigExecutor(value=houghCircleExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

