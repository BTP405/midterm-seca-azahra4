"""
Module: management_system.py

This module contains classes for managing employees, projects, and tasks in a fictional company.

Classes:
    - Employee: Represents an employee in the company.
    - Project: Represents a project in the company.
    - Task: Represents a task in the company.
    - ManagementSystem: Provides functionality to manage employees, projects, and tasks.
"""
import sys
from employee import Employee
from project import Project
from task import Task
class ManagementSystem(Employee, Project, Task):
    """
    Class representing a management system for employees, projects, and tasks in the company.

    Attributes:
        employees (list): List of employees in the system.
        projects (list): List of projects in the system.
        tasks (list): List of tasks in the system.
    """
    employees = []
    projects = []
    tasks = []
    def __init__(self):
        """
        Initialize a ManagementSystem object.
        """
        pass

    def add_employee(self, employee: Employee):
        """
        Add an employee to the management system.

        Args:
            employee (Employee): The employee to be added.
        """
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        """
        Remove an employee from the management system.

        Args:
            emp_id (str): The ID of the employee to be removed.
        """
        for match in self.employees:
            if match.emp_id == int(emp_id):
                del match

    def add_project(self, project: Project):
        """
        Add a project to the management system.

        Args:
            project (Project): The project to be added.
        """
        self.projects.append(project)

    def add_task(self, task: Task):
        """
        Add a task to the management system.

        Args:
            task (Task): The task to be added.
        """
        self.tasks.append(task)

    def assign_employee_to_project(self, emp_id, project_id):
        """
        Assign an employee to a project.

        Args:
            emp_id (str): The ID of the employee to be assigned.
            project_id (str): The ID of the project to which the employee will be assigned.
        
        Raises:
            ValueError: If employee or project is not found.
        """
        for emp in self.employees:
            if (emp_id == emp.emp_id):
                for proj in self.projects:
                    if (project_id == proj.project_id):
                        proj.assign_employee(emp)
            raise ValueError("Employee/Project not found!")
