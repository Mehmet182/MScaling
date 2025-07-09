
from sdks.novavision.src.helper.package import PackageHelper
from components.MScaling.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, MScaleExecutorOutputs, MScaleExecutorResponse, MScaleExecutor, OutputImage


def build_response(context):
    outputImage = OutputImage(value=context.image)

    mScalingExecutor = MScaleExecutorOutputs(outputImage=outputImage)

    mScaleExecutorResponse = MScaleExecutorResponse(outputs=mScalingExecutor)

    mScaleExecutor = MScaleExecutor(value=mScaleExecutorResponse)

    executor = ConfigExecutor(value=mScaleExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel


