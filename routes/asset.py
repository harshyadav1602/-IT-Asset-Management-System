import pandas as pd
from flask import send_file
from flask import Blueprint, render_template, request, redirect, url_for, session
from models.asset import (
    get_all_assets,
    add_asset,
    get_asset_by_id,
    update_asset,
    delete_asset,
    search_assets
)

asset_bp = Blueprint("asset", __name__)

@asset_bp.route("/assets")
def assets():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    keyword = request.args.get("search")

    if keyword:
        assets = search_assets(keyword)
    else:
        assets = get_all_assets()

    return render_template(
        "assets.html",
        assets=assets
    )

@asset_bp.route("/assets/add", methods=["GET", "POST"])
def add_asset_route():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        asset_id = request.form["asset_id"]
        asset_name = request.form["asset_name"]
        category = request.form["category"]
        brand = request.form["brand"]
        model = request.form["model"]
        status = request.form["status"]
        employee_id = request.form["employee_id"]

        add_asset(
            asset_id,
            asset_name,
            category,
            brand,
            model,
            status,
            employee_id
        )

        return redirect(url_for("asset.assets"))

    return render_template("asset_form.html")

@asset_bp.route("/assets/edit/<asset_id>", methods=["GET", "POST"])
def edit_asset(asset_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        update_asset(
            asset_id,
            request.form["asset_name"],
            request.form["category"],
            request.form["brand"],
            request.form["model"],
            request.form["status"],
            request.form["employee_id"]
        )

        return redirect(url_for("asset.assets"))

    asset = get_asset_by_id(asset_id)

    return render_template(
        "asset_form.html",
        asset=asset,
        edit=True
    )

@asset_bp.route("/assets/delete/<asset_id>")
def delete_asset_route(asset_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))

    delete_asset(asset_id)

    return redirect(url_for("asset.assets"))

@asset_bp.route("/assets/export/excel")
def export_asset_excel():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    assets = get_all_assets()

    df = pd.DataFrame(
        assets,
        columns=[
            "Asset ID",
            "Asset Name",
            "Category",
            "Brand",
            "Model",
            "Status",
            "Employee ID"
        ]
    )

    filepath = "exports/asset_report.xlsx"

    df.to_excel(filepath, index=False)

    return send_file(filepath, as_attachment=True)