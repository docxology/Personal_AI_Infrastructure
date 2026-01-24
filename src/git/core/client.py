"""
Git CLI Client

Wrapper for local git operations via subprocess.
"""

import logging
import subprocess
from typing import List, Optional, Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)


class GitError(Exception):
    """Exception raised for git command errors."""
    
    def __init__(self, message: str, returncode: int = None, stderr: str = None):
        self.returncode = returncode
        self.stderr = stderr
        super().__init__(message)


class GitClient:
    """
    Client for local git operations.
    
    Wraps git CLI commands with Python interface.
    
    Usage:
        client = GitClient("/path/to/repo")
        status = client.status()
        client.commit("feat: add feature")
    """
    
    def __init__(self, repo_path: Optional[str] = None):
        """
        Initialize git client.
        
        Args:
            repo_path: Path to git repository (default: current directory)
        """
        self.repo_path = Path(repo_path) if repo_path else Path.cwd()
        logger.debug(f"GitClient initialized for {self.repo_path}")
    
    def _run(self, args: List[str], check: bool = True) -> subprocess.CompletedProcess:
        """
        Run a git command.
        
        Args:
            args: Command arguments (without 'git' prefix)
            check: Raise on non-zero exit
            
        Returns:
            CompletedProcess result
        """
        cmd = ["git"] + args
        logger.debug(f"Running: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=check
            )
            return result
        except subprocess.CalledProcessError as e:
            raise GitError(
                f"Git command failed: {' '.join(cmd)}",
                returncode=e.returncode,
                stderr=e.stderr
            )
    
    def status(self, short: bool = False) -> str:
        """
        Get repository status.
        
        Args:
            short: Use short format
            
        Returns:
            Status output
        """
        args = ["status"]
        if short:
            args.append("-s")
        result = self._run(args)
        return result.stdout
    
    def log(
        self,
        n: int = 10,
        oneline: bool = False,
        format: Optional[str] = None
    ) -> str:
        """
        Get commit log.
        
        Args:
            n: Number of commits
            oneline: One line per commit
            format: Custom format string
            
        Returns:
            Log output
        """
        args = ["log", f"-n{n}"]
        if oneline:
            args.append("--oneline")
        if format:
            args.append(f"--format={format}")
        result = self._run(args)
        return result.stdout
    
    def diff(
        self,
        staged: bool = False,
        path: Optional[str] = None
    ) -> str:
        """
        Get diff output.
        
        Args:
            staged: Show staged changes
            path: Filter to specific path
            
        Returns:
            Diff output
        """
        args = ["diff"]
        if staged:
            args.append("--staged")
        if path:
            args.extend(["--", path])
        result = self._run(args)
        return result.stdout
    
    def branch(self, list_all: bool = False) -> str:
        """
        List branches.
        
        Args:
            list_all: Include remote branches
            
        Returns:
            Branch list
        """
        args = ["branch"]
        if list_all:
            args.append("-a")
        result = self._run(args)
        return result.stdout
    
    def checkout(self, ref: str, create: bool = False) -> str:
        """
        Checkout branch or commit.
        
        Args:
            ref: Branch name or commit hash
            create: Create new branch
            
        Returns:
            Checkout output
        """
        args = ["checkout"]
        if create:
            args.append("-b")
        args.append(ref)
        result = self._run(args)
        return result.stdout + result.stderr
    
    def add(self, paths: Optional[List[str]] = None, all: bool = False) -> str:
        """
        Stage files.
        
        Args:
            paths: Specific paths to add
            all: Add all changes
            
        Returns:
            Add output
        """
        args = ["add"]
        if all:
            args.append("-A")
        elif paths:
            args.extend(paths)
        else:
            args.append(".")
        result = self._run(args)
        return result.stdout
    
    def commit(self, message: str, all: bool = False) -> str:
        """
        Create a commit.
        
        Args:
            message: Commit message
            all: Stage all modified files
            
        Returns:
            Commit output
        """
        args = ["commit", "-m", message]
        if all:
            args.insert(1, "-a")
        result = self._run(args)
        return result.stdout
    
    def push(
        self,
        remote: str = "origin",
        branch: Optional[str] = None,
        force: bool = False
    ) -> str:
        """
        Push commits to remote.
        
        Args:
            remote: Remote name
            branch: Branch to push (default: current)
            force: Force push
            
        Returns:
            Push output
        """
        args = ["push", remote]
        if branch:
            args.append(branch)
        if force:
            args.append("--force")
        result = self._run(args)
        return result.stdout + result.stderr
    
    def pull(self, remote: str = "origin", branch: Optional[str] = None) -> str:
        """
        Pull from remote.
        
        Args:
            remote: Remote name
            branch: Branch to pull
            
        Returns:
            Pull output
        """
        args = ["pull", remote]
        if branch:
            args.append(branch)
        result = self._run(args)
        return result.stdout
    
    def fetch(self, remote: str = "origin", prune: bool = False) -> str:
        """
        Fetch from remote.
        
        Args:
            remote: Remote name
            prune: Prune deleted remote branches
            
        Returns:
            Fetch output
        """
        args = ["fetch", remote]
        if prune:
            args.append("--prune")
        result = self._run(args)
        return result.stdout + result.stderr
    
    def remote(self, verbose: bool = False) -> str:
        """
        List remotes.
        
        Args:
            verbose: Show URLs
            
        Returns:
            Remote list
        """
        args = ["remote"]
        if verbose:
            args.append("-v")
        result = self._run(args)
        return result.stdout
    
    def rev_parse(self, ref: str = "HEAD") -> str:
        """
        Get commit hash for reference.
        
        Args:
            ref: Reference to resolve
            
        Returns:
            Commit hash
        """
        result = self._run(["rev-parse", ref])
        return result.stdout.strip()
