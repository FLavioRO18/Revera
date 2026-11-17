import os
from pathlib import Path
import shutil
import subprocess

__author__ = "carunodev"

base = Path(__file__).resolve().parent.parent
sdk = Path(os.environ.get("ANDROID_HOME", str(Path.home() / "AppData/Local/Android/Sdk")))
ndk = sdk / "ndk/26.3.11579264/toolchains/llvm/prebuilt/windows-x86_64/bin"
env = os.environ.copy()
env["CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER"] = str(ndk / "aarch64-linux-android29-clang.cmd")
env["CC_aarch64_linux_android"] = env["CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER"]
env["AR_aarch64_linux_android"] = str(ndk / "llvm-ar.exe")
manifest = base / "audio-transport-rust/Cargo.toml"
subprocess.run(["cargo", "test", "--manifest-path", str(manifest)], env=env, check=True, timeout=600)
subprocess.run(["cargo", "build", "--locked", "--release", "--target", "aarch64-linux-android", "--manifest-path", str(manifest)], env=env, check=True, timeout=600)
out = base / "engine-android/src/main/jniLibs/arm64-v8a/liborpheon_audio.so"
out.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(base / "audio-transport-rust/target/aarch64-linux-android/release/liborpheon_audio.so", out)
print(out)
