from kfp import dsl
from kfp.dsl import component


@component
def hello_op(name: str) -> str:
    msg = f"Hello, {name}!"
    print(msg)
    return msg


@dsl.pipeline(name="hello-kfp-pipeline")
def hello_pipeline(name: str = "Bujji"):
    hello_op(name=name)


if __name__ == "__main__":
    from kfp import compiler
    import os

    os.makedirs("artifacts", exist_ok=True)
    out = "artifacts/hello_pipeline.yaml"
    compiler.Compiler().compile(
        pipeline_func=hello_pipeline,
        package_path=out,
    )
    print(f"Compiled: {out}")
