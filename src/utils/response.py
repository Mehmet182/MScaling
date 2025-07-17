
from sdks.novavision.src.helper.package import PackageHelper
from components.MScaling.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, MScaleExecutorOutputs, MScaleExecutorResponse, MScaleExecutor, OutputImage
from components.MScaling.src.models.PackageModel import HoughCircleExecutorOutputs,HoughCircleExecutorResponse ,HoughCircleExecutor,OutputImageA
from components.MScaling.src.models.PackageModel import GaussianBlurExecutorOutputs , GaussianBlurExecutorResponse,GaussianBlurExecutor
from components.MScaling.src.models.PackageModel import CatOrDogOutputs , CatOrDogResponse,CatOrDog



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
    outputImageA = OutputImageA(value=context.image2)

    houghCircleExecutorOutputs = HoughCircleExecutorOutputs(outputImage=outputImage,outputImageA=outputImageA)

    houghCircleExecutorResponse = HoughCircleExecutorResponse(outputs=houghCircleExecutorOutputs)

    houghCircleExecutor = HoughCircleExecutor(value=houghCircleExecutorResponse)

    executor = ConfigExecutor(value=houghCircleExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel




def build_response_CatOrDog(context):
    outputImage = OutputImage(value=context.image)

    catOrDogOutputs = CatOrDogOutputs(outputImage=outputImage)

    catOrDogResponse = CatOrDogResponse(outputs=catOrDogOutputs)

    catOrDog = CatOrDog(value=catOrDogResponse)

    executor = ConfigExecutor(value=catOrDog)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
