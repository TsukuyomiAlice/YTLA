import os


def merge_files(src_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, src_dir)

                # 写入文件路径作为分隔
                outfile.write(f"\n\n=== {relative_path} ===\n\n")

                # 读取并写入文件内容
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                except UnicodeDecodeError:
                    # 跳过二进制文件
                    outfile.write("[Binary file content skipped]")


if __name__ == "__main__":
    src_directory = "/src/core"
    output_file = "merged_output.txt"
    merge_files(src_directory, output_file)
    print(f"All files merged into {output_file}")

    src_directory = "/src/features/planManage"
    output_file = "merged_output2.txt"
    merge_files(src_directory, output_file)
    print(f"All files merged into {output_file}")