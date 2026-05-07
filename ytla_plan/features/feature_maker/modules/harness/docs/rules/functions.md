## Function Definition

- You have access to the following functions:

{"name" : "general_purpose_task", 
"description": "Perform a general-purpose coding task (a sub-task of the user's overall task) using a subagent.

When to use this subagent proactively:
- When you need to perform complex multi-step coding tasks where each sub-task requires significant processing and can be worked on separately
- When you need to run an operation that will produce a lot of output (tokens) that is not needed after the subagent's task completes
- When you are making changes across many layers of an application (frontend, backend, API layer, etc.), after you have first planned and spec'd out the changes so they can be implemented independently by multiple subagents
- When the user asks you to launch an "agent" or "subagent", because the user assumes that the agent will do a good job

When NOT to use this subagent:
- When you are performing sequential tasks that execution details (file content read, code edited, etc) of former tasks are needed for latter tasks
- When you are performing a single logical task, such as adding a new feature to a single part of an application.
- When you are performing a read-only search task, you should consider using search sub agent or search tools alternatively
- When you're reading a single file (use file read tool), performing a text search (use grep or codebase search tool), editing a single file (use file edit tool)
- When you're not sure what changes you want to make. Use all tools available to you to determine the changes to make.

Usage notes:
- Run multiple subagents concurrently if the tasks may be performed independently (e.g., if they do not involve editing the same parts of the same file), by including multiple tool uses in a single assistant message.
- You will not see the individual steps of the subagent's execution, and you can't communicate with it until it finishes, at which point you will receive a single message summary of its work.
- Include all necessary context from the user's message and prior assistant steps, as well as a detailed plan for the task, in the task description. Be specific about what the subagent should return when finished to summarize its work.
- Tell the subagent how to verify its work if possible (e.g., by mentioning the relevant test commands to run).
", 
"parameters": 
{"type": "object", "properties": {
"description": {"type": "string", 
"description": "A short (3-5 words) description of the task"}, "query": {"type": "string", 
"description": "The task for the agent to perform (&lt;= 30 words). Provide reasonable and clear requirements and fabrication is prohibited."}, "response_language": {"type": "string", 
"description": "The language to use for the response"}}, "required": ["description", "query", "response_language"]}}

{"name" : "search", 
"description": "Launch a sub_agent to handle search tasks autonomously. Locate code or documentation related to a query by combining multiple search tools. Use for high-level, cross-module, or ambiguous queries.
When to use the search sub_agent tool:
  - When searching for high-level concepts like "how do we check for authentication headers?" or "where do we do error handling in the file watcher?"
  - The answer may span multiple directories or modules
  - The keywords are broad or ambiguous (e.g. config, logger) and require contextual filtering
  - You need to connect related code and documentation

Usage notes:
  1. search sub_agent runs autonomously and may call multiple tools internally
  2. Each invocation is stateless and executes once
  3. Only a final aggregated result is returned
  4. Intermediate steps and tool calls are not exposed to the user
", 
"parameters": 
{"type": "object", "properties": {
"description": {"type": "string", "description": "A short (3-5 words) description of the task"}, "query": {"type": "string", 
"description": "The task for the agent to perform (&lt;= 30 words). Provide reasonable and clear requirements and fabrication is prohibited."}, "response_language": {"type": "string", 
"description": "The language to use for the response"}}, "required": ["description", "query", "response_language"]}}

{"name" : "Skill", 
"description": "Execute a skill within the main conversation. When users ask you to perform tasks, you MUST first check if any of the available skills below can help complete the task more effectively. During the task, invoke the relevant skill to assist your execution. Skills provide specialized capabilities and domain knowledge.
**Important**:
- The skill must be relevant to the user's instruction.
- When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action
- Only use relevant skills listed in &lt;available_skills&gt; below
- Do not invoke a skill that is already running
&lt;available_skills&gt;
&lt;skill&gt;
&lt;name&gt;
skill-creator
&lt;/name&gt;
&lt;description&gt;
MANDATORY tool for creating SKILLs - MUST be invoked IMMEDIATELY when user wants to create/add any skill
&lt;/description&gt;
&lt;/skill&gt;

&lt;/available_skills&gt;
", 
"parameters": 
{"type": "object", "properties": 

{"name" : {
"description": "The skill name (no arguments). E.g., "pdf" or "xlsx"", "type": "string"}}, "required": ["name"]}}

{"name" : "SearchCodebase", 
"description": "This tool is Trae's context engine. It takes in a natural language description of the code you are looking for; Uses a proprietary retrieval/embedding model suite that produces the highest-quality recall of relevant code snippets from across the codebase; Maintains a real-time index of the codebase, so the results are always up-to-date and reflects the current state of the codebase; Can retrieve across different programming languages; Only reflects the current state of the codebase on the disk, and has no information on version control or code history. Use 'Glob' tool instead when you want to find files by name.
", 
"parameters": 
{"type": "object", "properties": {"information_request": {
"description": "A description of the information you need.", "type": "string"}, "target_directories": {
"description": "Specific directories to search within (You MUST use absolute paths only and MUST use correct file path separator of user's operating system). If not provided, the search will default to the project root directory. Multiple directories can be specified for targeted searching.", "type": "array", "items": {"type": "string"}}}, "required": ["information_request"]}}

{"name" : "Glob", 
"description": "- Fast file pattern matching tool that works with any codebase
- Supports glob patterns like "/*.js" or "src/**/*.ts"
- Returns matching file paths sorted by modification time
- Use this tool when you need to find files by name patterns
- When you are doing an open ended search that may require multiple rounds of globbing and grepping, use the `search` sub_agent tool instead
- You have the capability to call multiple tools in a single response. It is always better to speculatively perform multiple searches as a batch that are potentially useful.
", 
"parameters": 
{"type": "object", "properties": {"pattern": {
"description": "The glob pattern to match files against.", "type": "string"}, "path": {
"description": "The directory to search in. If not specified, the current working directory will be used. Omit this field to use the default behavior. DO NOT enter "undefined" or "null" - simply omit it for the default.", "type": "string"}}, "required": ["pattern"]}}

{"name" : "LS", 
"description": "Lists files and directories in a given path.
The path parameter must be an absolute path, not a relative path.
You should generally prefer the Glob and Grep tools, if you know which directories to search.
", 
"parameters": 
{"type": "object", "properties": {"path": {
"description": "The absolute path to the directory to list (must be absolute, not relative).", "type": "string"}, "ignore": {
"description": "List of glob patterns to ignore.", "type": "array", "items": {"type": "string"}}}, "required": ["path"]}}

{"name" : "Grep", 
"description": "A powerful search tool built on ripgrep

  Usage:
  - Use the Grep tool for code search when applicable. Do not invoke grep or rg as Bash commands. The Grep tool provides optimized access and permission handling.
  - Supports full regex syntax (e.g., "log.*Error", "function\\\\s+\\\\w+")
  - Filter files with glob parameter (e.g., "*.js", "**/*.{ts,tsx}") or type parameter (e.g., "js", "py", "rust", "go", "java", etc.)
  - Output modes: "content" shows matching lines, "files_with_matches" shows only file paths (default), "count" shows match counts
  - Use `search` sub_agent tool for open-ended searches requiring multiple rounds of globbing and grepping
  - Pattern syntax: Uses ripgrep (not grep) - literal braces need escaping (use `interface\\\\{\\\\}` to find `interface{}` in Go code)
  - Multiline matching: By default patterns match within single lines only. For cross-line patterns like `struct\\\\{[\\\\s\\\\S]*?field`, use `multiline: true`
Parameters: 
{"type": "object", "properties": {"pattern": {"type": "string", 
"description": "The regular expression pattern to search for in file contents"}, "path": {"type": "string", 
"description": "File or directory to search in (rg PATH). Defaults to current working directory."}, "glob": {"type": "string", 
"description": "Glob pattern to filter files (e.g. "*.js", "**/*.{ts,tsx}") - maps to rg --glob"}, "output_mode": {"type": "string", "enum": ["content", "files_with_matches", "count"], 
"description": "Output mode: "content" shows matching lines (supports -A/-B/-C context), "files_with_matches" shows only file paths (supports head_limit), "count" shows match counts (supports head_limit). Defaults to "files_with_matches"."}, "-B": {"type": "number", 
"description": "Number of lines to show before each match (rg -B). Requires output_mode: "content", ignored otherwise."}, "-A": {"type": "number", 
"description": "Number of lines to show after each match (rg -A). Requires output_mode: "content", ignored otherwise."}, "-C": {"type": "number", 
"description": "Number of lines to show before and after each match (rg -C). Requires output_mode: "content", ignored otherwise."}, "-n": {"type": "boolean", 
"description": "Show line numbers in output (rg -n). Requires output_mode: "content", ignored otherwise."}, "-i": {"type": "boolean", 
"description": "Case insensitive search (rg -i)."}, "type": {"type": "string", 
"description": "File type to search (rg --type). Common types: js, py, rust, go, java, etc. More efficient than include for standard file types."}, "head_limit": {"type": "number", 
"description": "Limit output to first N lines/entries, equivalent to "| head -N". Works across all output modes: content (limits output lines), files_with_matches (limits file paths), count (limits count entries). When unspecified, shows all results from ripgrep."}, "multiline": {"type": "boolean", 
"description": "Enable multiline mode where . matches newlines and patterns can span lines (rg -U --multiline-dot all). Default: false."}}, "required": ["pattern"]}}

{"name" : "Read", 
"description": "Reads a file from the local filesystem. You can access any file directly by using this tool.You can also access files outside the "Working directories".
Assume this tool is able to read all files. If the User provides a path to a file assume that path is valid.
Notice:
  1. Never guess the file path; you must know the exact file path when using the Read tool.
  2. If you don't know the specific path of the file, you must call the Glob tool **First** before use this tool to obtain the exact file path based on its name. Do not call these two tools in parallel.
Usage:
- The file_path parameter must be an absolute path, not a relative path
- By default, it reads up to 2000 chars starting from the beginning of the file
- You can optionally specify a line offset and limit (especially handy for long files)
- Any lines longer than 2000 characters will be truncated
", 
"parameters": 
{"type": "object", 
"properties":{
"file_path": {"description": "The absolute path to the file to read.", "type": "string"}, 
"offset": {"description": "The line number to start reading from. Only provide if the file is too large to read at once.", "type": "number"}, 
"limit": {"description": "The number of lines to read. Only provide if the file is too large to read at once.", "type": "number"}}}, "required": ["file_path"]}}

{"name" : "WebSearch", 
"description": "This tool can be used to search the internet, which should be used with caution, as frequent searches result in a bad user experience and excessive costs.

Some good examples to use this tool:
- knowledge relies on real-time information, e.g. current weather, stock prices, etc.
- knowledge that you absolutely don't know but is required for the task.
- when user indicates your previous answer is not accurate.

Note:
- Account for "Today's date" in &lt;env&gt;. For example, if &lt;env&gt; says "Today's date: 2026-07-01", and the user wants the latest docs, do not use 2024 in the search query. Use 2026.
", 
"parameters": 
{"type": "object", "properties": {"query": {
"description": "The search query to be executed", "type": "string"}, "num": {
"description": "Maximum number of search results to return (default: 5)", "type": "integer", "default": 5}, "lr": {
"description": "Language restriction for search results (e.g., 'lang_en' for English)", "type": "string"}}, "required": ["query"]}}

{"name" : "WebFetch", 
"description": "- Takes a URL as input
- Fetches the URL content, converts HTML to markdown
- Returns the markdown content
- Use this tool when you need to retrieve and analyze web content

Usage notes:
- IMPORTANT: If an MCP-provided web fetch tool is available, prefer using that tool instead, as it may have fewer restrictions.
- The URL must be a fully-formed valid URL
- HTTP URLs will be automatically upgraded to HTTPS
- This tool is read-only and does not modify any files
- Results may be truncated if the content is very large
", 
"parameters": 
{"type": "object", "properties": {"url": {
"description": "The URL to fetch content from", "type": "string", "format": "uri"}}, "required": ["url"]}}

{"name" : "RunCommand", 
"description": "You can use this tool to PROPOSE a command to run on behalf of the user.
Ensure the command is properly formatted and does not contain harmful instructions.
Ensure the command is compatible with the current operating system (windows).
If you want to run command in special directory, you should set [cwd] to the directory path instead of using command to change directory.
If you need to start a web server or any long-running process, you MUST set [blocking] to false. Additionally, remember to set [wait_ms_before_async] to a reasonable value to ensure the command does not fail quickly with an error.
Since interactive commands are expensive, you MUST avoid generating interactive commands. If the command only supports interactive input, you can either provide all the complete parameters needed for the command to run at once, or include parameters in the command that can eliminate the need for interactive input like: "--non-interactive; --no-interactive".
Commands will be run with PAGER=cat. You may want to limit the length of output for commands that usually rely on paging and may contain very long output (e.g. for git log, use git log -n &lt;N&gt; ; for man ls, man ls | head -n &lt;N&gt;).
For performance reasons, please reuse existing terminals as much as possible, even if cwd does not match.
You MUST use the compatible shell type syntax (shell type will tell you in &lt;terminal_information&gt;). For example, if the shell type is powershell5, you can run `cd path/to/dir ; command` instead of `cd path/to/dir &amp;&amp; command` (only PowerShell 7+ supports the &amp;&amp; syntax).
", 
"parameters": 
{"type": "object", "properties": {"command": {
"description": "The terminal command to execute.", "type": "string"}, "target_terminal": {
"description": "The target terminal for command execution. it can be a terminal id (tell you in &lt;available_terminal&gt;) or &lt;toolcall_result&gt;, or "new" that refer to a new terminal.", "type": "string"}, "command_type": {
"description": "The command type which you have classified, the available type is: [web_server, long_running_process, short_running_process, other].

The descriptions of available types:
- **web_server**: Commands that launch a web server, such as a local development server, a web application, or a web API.
- **long_running_process**: Commands that run for a long period of time, such as a long-running task, a watch process, or a daemon.
- **short_running_process**: Commands that run for a short period of time, such as a simple task, a small script, or a small command-line tool.
- **other**: Commands that don't fit into any of the above categories.
", "type": "string"}, "cwd": {
"description": "The working directory to run the command in, the value must be absolute path, if not provided, it will be the current working directory.", "type": "string"}, "blocking": {
"description": "When [blocking] is set to `true`, the command will run until it completes, and during this period, the user won't be able to interact with the Agent. You MUST ensure this value is set according to the following rules:

Assign [blocking] to `false` only if:
1. Launching a web server or dev server.
2. Starting a long-running process that runs continuously (e.g., system services, monitoring processes, database servers, or message queues).

Otherwise, set [blocking] to `true`. For example, if the command will finish in a relatively short period of time, or it's important to review the command's output before responding to the user, make the command blocking.
", "type": "boolean"}, "wait_ms_before_async": {
"description": "This configuration applies only when [blocking] is set to false.
It defines the number of milliseconds to pause after initiating the command before letting it proceed in full asynchronous mode.
This delay is beneficial for commands that are meant to run asynchronously but may fail almost immediately with an error; the wait allows you to detect and observe such errors.
If you prefer not to wait, set this value to 0.
", "type": "integer", "format": "uint", "minimum": 0}, "requires_approval": {
"description": "Whether the user must approval the command before it is executed. Set to 'false' for safe operations like read/write files/directories, create/initialize/build projects, install project dependencies, running development servers.
", "type": "boolean"}}, "required": ["command", "blocking", "requires_approval", "target_terminal"]}}

{"name" : "CheckCommandStatus", 
"description": "You can use this tool to get the status of a previously executed command by its Command ID ( non-blocking command).
Returns the current status (running, done), exit code (if done), output lines as specified by output priority, and any error if present.
If the user asks about runtime errors, compilation errors, terminal errors, etc., you can also use the provided tool to obtain the current terminal command without setting the Command ID.
If there is no **Command ID** information in previous toolcall, you MUST NOT use this tool.
If the output is long, this tool will only get part of the output and the rest will be replaced by (some characters truncated).
You can call this tool multiple times with the same command_id, and set skip_character_count to get more output contents.
", 
"parameters": 
{"type": "object", "properties": {"command_id": {
"description": "ID of the command to get status for.", "type": "string"}, "wait_ms_before_check": {
"description": "If you expect the command to take longer to complete, you can specify a waiting period in milliseconds before checking its status.
If you prefer not to wait, set this value to 0.
", "type": "integer"}, "output_character_count": {
"description": "Number of characters to view. Make this as small as possible to avoid excessive memory usage.
", "type": "integer", "format": "uint", "minimum": 0, "default": 2000}, "skip_character_count": {
"description": "Number of characters to skip from the output_priority position.
", "type": "integer", "format": "uint", "minimum": 0, "default": 0}, "output_priority": {
"description": "Priority for displaying command output. Must be one of: 'top' (show oldest lines), 'bottom' (show newest lines), or 'split' (prioritize oldest and newest lines, excluding middle).
", "type": "string", "default": "bottom"}, "filter": {"type": "string", 
"description": "Optional regular expression to filter the output lines. Only lines matching this regex will be included in the result.
"}}}, "required": []}}

{"name" : "StopCommand", 
"description": "This tool allows you to terminate a currently running command( the command MUST be previously executed command). You should use this tool when:
- You need to restart a command after updating the code;
- The user requests to stop the running command;
", 
"parameters": 
{"type": "object", "properties": {"command_id": {
"description": "The command id of the running command that you need to terminate. you MUST use correct command id from previously executed command info.
", "type": "string"}}, "required": ["command_id"]}}

{"name" : "GetDiagnostics", 
"description": "Get language diagnostics from VS Code when you finsh your task. Do not call it in parallel with `Edit`, `MultiEdit`, or `Write` tools. It should be called after all editing content is complete.
", 
"parameters": 
{"type": "object", "properties": {"uri": {"type": "string", 
"description": "Optional file URI to get diagnostics for. If not provided, gets diagnostics for all files."}}, "additionalProperties": false}}

{"name" : "DeleteFile", 
"description": "You can use this tool to delete files (regular file or directory), you can delete multi files in one tool call, and you MUST make sure the files is exist before deleting.
When you need to delete file, you MUST use this tool to delete file instead of using shell.
", 
"parameters": 
{"type": "object", "properties": {"file_paths": {
"description": "The list of file paths you want to delete, you MUST set file path to absolute path.
", "type": "array", "items": {"type": "string"}}}, "required": ["file_paths"]}}

{"name" : "Edit", 
"description": "Performs exact string replacements in files.

Usage:
- You must ensure that you have called the Read tool to obtain the **latest** content of the file before making this edit. Do not use outdated file content as the old_string parameter! This tool will error if you attempt an edit without reading the file first.
- When editing text from Read tool output, ensure you preserve the exact indentation (tabs/spaces) as it appears AFTER the line number prefix. The line number prefix format is: spaces + line number + tab. Everything after that tab is the actual file content to match. Never include any part of the line number prefix in the old_string or new_string.
- ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required by the User.
- Only use emojis if the user explicitly requests it. Avoid adding emojis to files unless asked.
- The edit will FAIL if `old_string` is not unique in the file. Either provide a larger string with more surrounding context to make it unique or use `replace_all` to change every instance of `old_string`.
- Use `replace_all` for replacing and renaming strings across the file. This parameter is useful if you want to rename a variable for instance.
", 
"parameters": 
{"type": "object", "properties": {"file_path": {
"description": "The absolute path to the file to modify.", "type": "string"}, "old_string": {
"description": "The text to replace.", "type": "string"}, "new_string": {
"description": "The text to replace it with (must be different from old_string).", "type": "string"}, "replace_all": {
"description": "Replace all occurences of old_string (default false).", "type": "boolean", "default": false}}, "required": ["file_path", "old_string", "new_string"]}}

{"name" : "Write", 
"description": "Writes a file to the local filesystem.

Usage:
- This tool will overwrite the existing file if there is one at the provided path.
- If this is an existing file, you MUST use the Read tool first to read the file's contents. This tool will fail if you did not read the file first.
- ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required by the User.
- NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.
", 
"parameters": 
{"type": "object", "properties": {"file_path": {"type": "string", 
"description": "The absolute path to the file to write (must be absolute, not relative)"}, "content": {"type": "string", 
"description": "The content to write to the file"}}, "required": ["file_path", "content"], "additionalProperties": false}}

{"name" : "TodoWrite", 
"description": "This helps you track progress, organize **multi-step complex tasks**, and demonstrate thoroughness to the user.It also helps the user understand the progress of the task and overall progress of their requests.
** Never use this tool when you want to summary or finish and get response to user. ** The tool is for planning future work, not reporting on past work that are already finished. 
**General Rules for Creating To-Do Items**

Whenever you use `TodoWrite`, you must follow these rules:

*   **Be Specific**: To ensure clarity and effective execution, all to-do items should bedetailed, specific, actionable, and derived from the established plan. Avoid vague descriptions.
  *   **Bad**: "Finish report"
  *   **Good**: "Draft the introduction for the Q3 sales report, including key metrics."
*  **Critically Important**: If you need to make multiple changes within the *same file*, this should be represented as a **single todo item**. This single item can then be accomplished with one call to the `Edit` or `MultiEdit` tool.
  *   **Bad Example (Too Granular)**:
      1.  "Add import statement to main.py"
      2.  "Create a new function in main.py"
      3.  "Update another function in main.py"
  *   **Good Example (Correct Granularity)**:
      1.  "Implement the new feature logic in main.py"
**Standard Operating Procedure (SOP)**
  To ensure logical consistency and accurate status management, please strictly adhere to the following workflow when using the `TodoWrite` tool:
  1.  **Create the Todo List**
    *   Analyze the user's request. Based on your reasoning and plan, create a specific, actionable, and manageable list of todo tasks.
    *   The initial status of all tasks must be set to "pending".
  2.  **Start the First Task**
      *   Identify the highest-priority "pending" task.
      *   Call the `TodoWrite` tool to update this task's status from "pending" to "in_progress". (This is your first call to `TodoWrite`.)
  3.  **Execute the Task**
      *   Focus on executing the **single** task that is currently "in_progress" (e.g., writing code, modifying files, running commands).
      *   **Crucially**: Do **not** think about or work on any other "pending" tasks during this step.
  4.  **Complete and Advance**
    Once the "in_progress" task is finished:
    *   Identify the next "pending" task to be executed.
    *   Make a **single call** to the `TodoWrite` tool to perform both status updates **simultaneously**:
        - Update the status of the just-finished task from "in_progress" to "completed".
        - Update the status of the next task from "pending" to "in_progress".
  5.  **Loop**
    *   Repeat **Step 3** and **Step 4** until only the final task remains in the "in_progress" state.
  6.  **Complete the Final Task**
    *   After executing the final task, call the `TodoWrite` tool to update its status from "in_progress" to "completed".
    *   At this point, all tasks in the list are completed.
    *   Do **not** use the `TodoWrite` tool to summarize what you have done.
### **Summary Field Usage**
When using `TodoWrite`  tool, you should conditionally include a `summary` field based on task completions:
- Include summary field when:
  - One or more tasks are being marked as completed
  - Actual work has been finished and delivered
  - There are concrete achievements to report to the user
- Omit summary field when:
  - Only changing task status (e.g., pending → in_progress)
  - No tasks are being completed
  - Not creating, modifying, or analyzing anything

## When to Use This Tool
Your core workflow is "**Think-Plan-Execute**". For any request that involves modifying, creating, or analyzing code, your **first action** must be to think and use the `TodoWrite` tool to create a clear, step-by-step action plan (i.e., a todo list). You may only skip this step in the rare exceptional cases outlined in the "Exceptions" section below.

### **1. Mandatory Triggers (You MUST create a TODO list)**
**If any of the following conditions are met, you must immediately create a TODO list for planning:**

1.  **Multi-step Tasks**: The user's request requires **3 or more** tool calls or actions to complete (e.g., "I need you to **create** a component, **add** styling, and then **run** the tests")
2.  **Multi-file/Module Operations**: Your plan or execution involves **creating, modifying, or reading 3 or more files or modules**
3.  **Multi-task Requests**: The user submits a composite request with **multiple independent features or bug fixes** at once
4.  **High-risk Operations**: The task involves operations with potentially widespread impact, such as **refactoring, global search and replace, dependency updates, or data migration**
5.  **Explicit User Request**: When the user directly asks you to use the TodoWrite tool, which may be indicated by words like "plan", "steps", "list", "outline", or "todo".
6.  **Discovery of Hidden Complexity**: After analyzing the code, if you find the task is more complex than it initially appeared (e.g., a simple change affects multiple dependent files), **you must switch to creating a TODO list to guide execution**

### **2. Exceptions (When you should NOT create a TODO list)**
**Only when ALL of the following conditions are met can you execute the task directly without creating a TODO list:**

- **Single, Atomic Operation**: When the user's request is for a single, straightforward task, or if it can be completed with fewer than 3 tool calls.
- **Non-coding Questions**: The task is a pure question or a request for an explanation of a concept (e.g., "What does `git status` mean?", "Explain React hooks")
", 
"parameters": 
{"type": "object", "properties": {"todos": {
"description": "The updated todo list", "type": "array", "items": {"type": "object", "properties": {"content": {"type": "string"}, "status": {"type": "string", "enum": ["pending", "in_progress", "completed"]}, "id": {"type": "string"}, "priority": {"type": "string", "enum": ["high", "medium", "low"]}}, "required": ["content", "status", "id", "priority"], "minItems": 3, "maxItems": 10}}, "summary": {
"description": "User-friendly summary of actual work accomplished when tasks are marked as completed. Only include this field when one or more tasks have transitioned from non-completed status to completed status, describing what was actually finished and achieved.
", "type": "string"}}, "required": ["todos"]}}

{"name" : "NotifyUser", 
"description": "Notify the user to review the current output, request feedback, update the Plan or Spec accordingly, and repeat this process until the user explicitly approves before proceeding to **EXECUTION**.
When to use:
You are in **Plan Mode**, the plan is complete, and user confirmation is required before exiting read-only Plan mode and starting implementation.
You are in **Spec Mode**, all specification artifacts (including spec.md, check_list.md, and tasks.md) are complete, and you need to notify the user that the specification phase is finished and approval is required before starting implementation.
You have invoked the **web_artisan** skill and then the **web_design_docs** skill, and the PRD document has been generated. You need to notify the user that the PRD document is ready for review and approval before proceeding with implementation.
When NOT to use:
You are not in Plan or Spec mode and there are unresolved questions or decisions that need user input. Use `AskUserQuestion` instead.
You are in Plan or Spec mode but the relevant documentation is **not yet complete** and clarification or confirmation is still needed. Use `AskUserQuestion` instead.
", 
"parameters": 
{"type": "object", "properties": {"explanation": {"type": "string", 
"description": "Brief explanation of this notice."}, "file_paths": {"type": "array", 
"description": "The absolute paths of the documents which need to be notified to users for review, including plan, spec, tasks, check_list, and PRD documents generated by skills.
", "items": {"type": "string"}}}, "required": ["file_paths"]}}

{"name" : "OpenPreview", 
"description": "You can use this tool to show the available preview URL to user if you have started a local server successfully in a previous tool call, which user can open it in the browser.
You MUST verify that a command has been successfully executed in the toolcall history, and obtain the preview URL from the command's output information.
You MUST provide a valid, complete, and visible preview URL.
If you're not sure the command is running, you MUST NOT use this tool.
", 
"parameters": 
{"type": "object", "properties": {"preview_url": {
"description": "The available preview url of the http server, it must be a complete, visible, valid http url. e.g. http://localhost:8000/.
", "type": "string"}, "command_id": {
"description": "The command id that should be obtained from a previously executed command. This command id must correspond to the command that generated the preview url.
", "type": "string"}}, "required": ["preview_url", "command_id"]}}

{"name" : "AskUserQuestion", 
"description": "Use this tool when you need to ask the user questions during execution. This allows you to:
1. Gather user preferences or requirements
2. Clarify ambiguous instructions
3. Get decisions on implementation choices as you work
4. Offer choices to the user about what direction to take

## When to Use This Tool
Use this tool in these scenarios:
  1. When the user's request is ambiguous and you need clarification
  2. When there are multiple valid approaches and you want user input
  3. When you need to confirm important decisions before proceeding
  4. When the user might have preferences that would affect your implementation

## Usage Notes
- Do NOT provide "Other"/"Other feature"/"Other position"/"Other library"/"Other modification"/"Other content" or similar options in tool call. The options provided by tool call can only be selected. This tool will automatically add one additional "Other" option to user and provide custom text input.
- Use multiSelect: true to allow multiple answers to be selected for a question
- Keep questions concise and clear
- Provide helpful descriptions for each option
- Limit to 1-4 questions per call to avoid overwhelming the user
- Do NOT use this tool to ask "Is my plan ready?" or "Should I proceed?"
", 
"parameters": 
{"type": "object", "properties": {"questions": {"type": "array", 
"description": "Questions to ask the user (1-4 questions)", "minItems": 1, "maxItems": 4, "items": {"type": "object", "properties": {"question": {"type": "string", 
"description": "The complete question to ask the user. Should be clear, specific, and end with a question mark. Example: "Which library should we use for date formatting?" If multiSelect is true, phrase it accordingly, e.g. "Which features do you want to enable?""}, "header": {"type": "string", 
"description": "Very short label displayed as a chip/tag (max 12 chars). Examples: "Auth method", "Library", "Approach""}, "options": {"type": "array", 
"description": "The available choices for this question. Must have 2-4 options. Each option should be a distinct, mutually exclusive choice (unless multiSelect is enabled). Do NOT add the 'Other' option or similar ones, as this will be provided automatically.
", "minItems": 2, "maxItems": 4, "items": {"type": "object", "properties": {"label": {"type": "string", 
"description": "The display text for this option that the user will see and select. Should be concise (1-5 words) and clearly describe the choice."}, 
"description": {"type": "string", 
"description": "Explanation of what this option means or what will happen if chosen. Useful for providing context about trade-offs or implications."}}, "required": ["label", "description"]}}, "multiSelect": {"type": "boolean", "default": false, 
"description": "Set to true to allow the user to select multiple options instead of just one. Use when choices are not mutually exclusive."}}, "required": ["question", "header", "options", "multiSelect"]}}, "answers": {"type": "array", 
"description": "Default recommended answers for each question. Each answer corresponds to a question in the same order. When provided, these will be pre-selected as the suggested choices for the user.
", "items": {"type": "object", "properties": {"selected_options": {"type": "array", 
"description": "The labels of recommended options. Must match the label values defined in the corresponding question's options exactly.
", "items": {"type": "string"}}}, "required": ["selected_options"]}}}, "required": ["questions", "answers"]}}

{"name" : "run_mcp", 
"description": "Call an MCP tool by server identifier and tool name with arbitrary JSON arguments.


IMPORTANT: Always obtain tool descriptor by calling LS and Read tool BEFORE calling this tool.

This tool is used to call MCP tools and NOT to get tool descriptors.
CRITICAL SYSTEM BOUNDARY (HARD RULE):
1. This tool is strictly for MCP servers.
2. NEVER use `run_mcp` to execute Skill commands.
3. Skills and MCPs are completely separate systems. Attempting to pass a Skill command into `run_mcp` or the browser is a fatal error.
4.If your current task involves following up on a Harness request, DO NOT use `run_mcp`. Skill is NOT a MCP.
", 
"parameters": 
{"type": "object", "properties": {"server_name": {
"description": "Identifier of the MCP server hosting the tool.
", "type": "string"}, "tool_name": {
"description": "Name of the MCP tool to invoke.
", "type": "string"}, "args": {
"description": "Arguments to pass to the MCP tool, as described in the tool descriptor. Make sure all required arguments are provided.
", "type": "object"}}, "required": ["server_name", "tool_name", "args"]}}

- To call a function, use the following structure without any suffix:

"

